from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import update_last_login, User

from users.serializers import RegisterSerializer, UserProfileSerializer, LoginSerializer, UserSerializer, \
    PasswordResetSerializer, PasswordResetConfirmSerializer


class CheckCredentialsView(APIView):
    def post(self, request):
        print("hello")
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]  # Allow access to anyone without a token

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@require_POST
def PasswordResetView(request):
    # Load the JSON data from request.body
    data = json.loads(request.body)
    email = data.get('email', None)

    # Pass the email directly to the serializer
    serializer = PasswordResetSerializer(data={'email': email}, context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "Password reset link has been sent to your email."}, status=status.HTTP_200_OK)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    permission_classes = []  # No authentication required

    @method_decorator(csrf_exempt)  # CSRF exemption
    @method_decorator(require_POST)  # Allow only POST requests
    def post(self, request, uidb64, token):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uidb64, token)
            return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# @csrf_exempt
# @require_POST
# def login_view(request):
#     data = json.loads(request.body)
#     username = data['username']
#     password = data['password']
#
#     user = authenticate(request, username=username, password=password)
#     print(username, password)
#     if user is not None:
#         login(request, user)
#         user_data = UserSerializer(user).data
#         return JsonResponse({'user': user_data})
#     else:
#         return JsonResponse({'message': 'Invalid credentials'}, status=400)


@csrf_exempt
@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        # Update the last login
        update_last_login(None, user)

        user_data = UserSerializer(user).data
        return JsonResponse({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user_data
        })
    else:
        return JsonResponse({'message': 'Invalid credentials'}, status=400)


# @csrf_exempt
# @require_POST
# def logout_view(request):
#     logout(request)
#     return JsonResponse({'message': 'Logout successful'})

@csrf_exempt
@require_POST
def logout_view(request):
    return JsonResponse({'message': 'Logout successful'})


# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def current_user_view(request):
#     user = request.user
#     return JsonResponse({
#         'username': user.username,
#         'email': user.email,
#         'role': user.profile.role
#     })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    user = request.user
    user_data = UserSerializer(user).data
    return JsonResponse(user_data)
