from django.urls import path
from .views import *

urlpatterns = [
    path('check-credentials/', CheckCredentialsView.as_view(), name='check-credentials'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('current-user/', current_user_view, name='current_user'),
    path('password-reset/', PasswordResetView, name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),

]
