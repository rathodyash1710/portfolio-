# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Profile, SkillCategory, Experience, Project, Education, Certification
)
from .serializers import (
    PortfolioSerializer, ProfileSerializer, SkillCategorySerializer,
    ExperienceSerializer, ProjectSerializer, EducationSerializer, CertificationSerializer
)

class PortfolioView(APIView):
    """
    Get complete portfolio data
    """
    def get(self, request):
        try:
            profile = Profile.objects.first()
            skills = SkillCategory.objects.prefetch_related('skills').all()
            experience = Experience.objects.prefetch_related('achievements').all()
            projects = Project.objects.prefetch_related('technologies').all()
            education = Education.objects.all()
            certifications = Certification.objects.all()

            data = {
                'profile': ProfileSerializer(profile).data if profile else None,
                'skills': SkillCategorySerializer(skills, many=True).data,
                'experience': ExperienceSerializer(experience, many=True).data,
                'projects': ProjectSerializer(projects, many=True).data,
                'education': EducationSerializer(education, many=True).data,
                'certifications': CertificationSerializer(certifications, many=True).data,
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Individual CRUD views for admin panel or separate management

class ProfileDetailView(APIView):
    def get(self, request):
        profile = Profile.objects.first()
        if profile:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        profile = Profile.objects.first()
        if profile:
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)


