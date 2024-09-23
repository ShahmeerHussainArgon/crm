from django.contrib import admin
from .models import Project, Platform, TechStack, Keyword, Document

admin.site.register(Project)
admin.site.register(Platform)
admin.site.register(TechStack)
admin.site.register(Keyword)
admin.site.register(Document)