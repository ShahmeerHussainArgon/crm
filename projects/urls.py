from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, PlatformViewSet, TechStackViewSet, KeywordViewSet, DocumentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'platforms', PlatformViewSet)
router.register(r'techstacks', TechStackViewSet)
router.register(r'keywords', KeywordViewSet)
router.register(r'documents', DocumentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
