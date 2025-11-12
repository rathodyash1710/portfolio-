from rest_framework import serializers
from .models import (
    Profile, SkillCategory, Skill, Experience, Achievement,
    Project, Technology, Education, Certification
)

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']

class SkillCategorySerializer(serializers.ModelSerializer):
    items = SkillSerializer(many=True, read_only=True, source='skills')

    class Meta:
        model = SkillCategory
        fields = ['category', 'items']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['description']

class ExperienceSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ['title', 'company', 'duration', 'description', 'achievements']

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):
    tech = TechnologySerializer(many=True, read_only=True, source='technologies')

    class Meta:
        model = Project
        fields = ['title', 'description', 'tech', 'github', 'demo']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'duration', 'details']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['name', 'issuer', 'year']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'title', 'bio', 'email', 'phone', 'linkedin', 'github', 'location']

class PortfolioSerializer(serializers.Serializer):
    profile = ProfileSerializer(read_only=True)
    skills = SkillCategorySerializer(many=True, read_only=True)
    experience = ExperienceSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    certifications = CertificationSerializer(many=True, read_only=True)