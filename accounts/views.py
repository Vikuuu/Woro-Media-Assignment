from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserAccountSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .email import send_confirmation_email

User = get_user_model()


class RegistrationView(APIView):
    
    def post(self, request, format=None):
        try:
            data = request.data 
            serializer = UserAccountSerializer(data=data)
            
            if not serializer.is_valid():
                return Response(
                    {"error": serializer.errors}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            user = serializer.create(serializer.validated_data)
            user = UserAccountSerializer(user)
            
            send_confirmation_email(serializer.validated_data["email"])
            
            return Response(
                {"user": user.data,
                "message": "Check your email for verification"},
                status=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            return Response(
                {"error": "Something went wrong while registering the user"
                + str(e)  },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            

class LoginView(APIView):
    
    def post(self, request, format=None):
        try:
            data = request.data
            serializer = UserLoginSerializer(data=data)
            
            if not serializer.is_valid():
                return Response(
                    {"error": serializer.errors}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            
            user = authenticate(request, email=email, password=password)
            
            if user:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)
                
                return Response({
                    'user': serializer.data,
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": "Invalid email or password"
                },status=status.HTTP_401_UNAUTHORIZED)
                
        except Exception as e:
            return Response(
                {"error": "Something went wrong while logging in " 
                + str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            

class VerifyEmailView(APIView):
    
    def get(self, request, token, format=None):
        user = get_object_or_404(User, confirmation_token=token)
        user.is_verified = True
        user.save()
        
        return Response({
            "message": "Email Verification successful"
        },status=status.HTTP_200_OK)