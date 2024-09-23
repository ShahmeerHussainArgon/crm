from django.db import models
from django.contrib.auth.models import User


class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TechStack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=255,default="document-1")
    file = models.FileField(upload_to='documents/')


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    client_name = models.CharField(max_length=255)
    responsible_person = models.ForeignKey(User, related_name='responsible_projects', on_delete=models.CASCADE)
    development_team = models.ManyToManyField(User, related_name='team_projects')
    tech_stack = models.ManyToManyField(TechStack, related_name='projects')
    project_documents = models.ManyToManyField(Document, related_name='projects', blank=True)
    git_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)
    figma_link = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=255)
    keywords = models.ManyToManyField(Keyword, related_name='projects', blank=True, null=True)
    logo_icon = models.ImageField(upload_to='project_logos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    platform = models.ManyToManyField(Platform, related_name='projects')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    server_link = models.URLField(blank=True, null=True)
    server_email = models.EmailField(blank=True, null=True)
    server_password = models.CharField(max_length=128, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)  # New rating field

    def __str__(self):
        return self.name
