from django.contrib import admin
from .models import (
    Profile, SkillCategory, Skill, Experience, Achievement,
    Project, Technology, Education, Certification
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'updated_at']
    search_fields = ['name', 'email']

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ['name', 'order']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'order', 'created_at']
    list_editable = ['order']
    inlines = [SkillInline]
    ordering = ['order']

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 1
    fields = ['description', 'order']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'duration', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['title', 'company']
    inlines = [AchievementInline]
    ordering = ['order']

class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 1
    fields = ['name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'github', 'demo', 'created_at']
    list_editable = ['order']
    search_fields = ['title', 'description']
    inlines = [TechnologyInline]
    ordering = ['order']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'duration', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['degree', 'institution']
    ordering = ['order']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'year', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['name', 'issuer']
    ordering = ['order']