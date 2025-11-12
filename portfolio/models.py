from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class SkillCategory(models.Model):
    category = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Skill Categories"

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.category.category} - {self.name}"

    class Meta:
        ordering = ['order']

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['order']

class Achievement(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='achievements')
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.experience.title} - Achievement"

    class Meta:
        ordering = ['order']

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github = models.URLField(blank=True, null=True)
    demo = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Technology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.project.title} - {self.name}"

    class Meta:
        verbose_name_plural = "Technologies"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Education"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.issuer}"

    class Meta:
        ordering = ['order']