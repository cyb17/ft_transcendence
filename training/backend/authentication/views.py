from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsOwner
from django.contrib.auth import logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class ListUsers(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

class CreateUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [AllowAny]

class UserOperations(generics.RetrieveUpdateDestroyAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = CustomUserSerializer
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated, IsOwner]
     
@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    