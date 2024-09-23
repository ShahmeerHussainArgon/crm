from rest_framework import serializers
from .models import Job
from projects.models import Project, TechStack

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tech_stack = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=TechStack.objects.all()
    )

    class Meta:
        model = Project
        fields = '__all__'
