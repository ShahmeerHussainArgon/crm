from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import JobProcessingAPIView, JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')


urlpatterns = [
    path('process-job/', JobProcessingAPIView.as_view(), name='process-job'),
    path('', include(router.urls)),  # Correct path for router URLs

]
