from rest_framework import serializers
from .models import Project, Platform, TechStack, Keyword, Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    project_documents = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False
    )
    documents = DocumentSerializer(many=True, source='project_documents', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def get_documents(self, obj):
        return [document.file.url for document in obj.project_documents.all()]

    def create(self, validated_data):
        development_team = validated_data.pop('development_team', [])
        tech_stack = validated_data.pop('tech_stack', [])
        platform = validated_data.pop('platform', [])
        keywords = validated_data.pop('keywords', [])
        project_documents = validated_data.pop('project_documents', [])

        project = Project.objects.create(**validated_data)

        # Set ManyToMany fields
        project.development_team.set(development_team)
        project.tech_stack.set(tech_stack)
        project.platform.set(platform)
        project.keywords.set(keywords)

        # Handle file uploads for project_documents
        if project_documents:
            document_instances = []
            for file in project_documents:
                document = Document.objects.create(file=file,name=file.name)  # Create Document instances
                document_instances.append(document)
            project.project_documents.set(document_instances)  # Assign created Document instances

        return project

    def update(self, instance, validated_data):
        development_team = validated_data.pop('development_team', [])
        tech_stack = validated_data.pop('tech_stack', [])
        platform = validated_data.pop('platform', [])
        keywords = validated_data.pop('keywords', [])
        project_documents = validated_data.pop('project_documents', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Set ManyToMany fields
        if development_team:
            instance.development_team.set(development_team)
        if tech_stack:
            instance.tech_stack.set(tech_stack)
        if platform:
            instance.platform.set(platform)
        if keywords:
            instance.keywords.set(keywords)

        # Handle file uploads for project_documents
        if project_documents:
            document_instances = []
            for file in project_documents:
                document = Document.objects.create(file=file)
                document_instances.append(document)
            instance.project_documents.set(document_instances)

        return instance

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'
