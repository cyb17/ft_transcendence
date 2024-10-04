from .models import CustomUser
from .serializers import CustomUserSerializer#, UserLoginSerializer
# from django.contrib.auth import authenticate
from django.contrib.auth import logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
	permission_classes = [IsAuthenticated]
     
@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    
# class UserLogin(generics.GenericAPIView):
#     # permission_classes = [AllowAny]
#     serializer_class = UserLoginSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 # Génération du token JWT
#                 token_serializer = TokenObtainPairSerializer.get_token(user)
#                 access_token = str(token_serializer.access_token)
#                 refresh_token = str(token_serializer)
#                 return Response({'access': access_token, 'refresh': refresh_token}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'Forbidden': 'User is not active'}, status=status.HTTP_403_FORBIDDEN) 
#         else:
#             return Response({"error": "Login failed. Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
