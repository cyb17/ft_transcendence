from .models import User
from .permissions import IsOwner
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from django.utils.crypto import get_random_string
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from django.urls import reverse
from django.core.mail import send_mail

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	authentication_classes = [JWTAuthentication]
    
	def get_permissions(self):
		if self.action == 'create':
			permission_classes = [AllowAny]
		elif self.action in ['update', 'destroy', 'partial_update', 'retrieve']:
			permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
		else:
			permission_classes = [IsAdminUser]
		return [permission() for permission in permission_classes]

class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh_token')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise InvalidToken('No valid token found in cookie \'refresh_token\'')


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            # cookie_max_age = 10 # 60s
            cookie_max_age = 3600 * 24 * 14 # 14 days
            response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True)
            del response.data['refresh']
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
	serializer_class = CookieTokenRefreshSerializer
            
	def finalize_response(self, request, response, *args, **kwargs):
		if response.data.get('refresh'):
			# cookie_max_age = 10 # 60s
			cookie_max_age = 3600 * 24 * 14  # 14 days
			response.set_cookie('refresh_token', response.data['refresh'], max_age=cookie_max_age, httponly=True)
			del response.data['refresh']
		return super().finalize_response(request, response, *args, **kwargs)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def send_verification_email(request):
	from_mail = "ponggame@mail.com"
	user_email = request.data.get('email')
	# verification_token = get_random_string(length=32)
	verification_token = "true_email"

	try:
		verification_link = f"http://localhost:8000/auth/email-verified/?token={verification_token}"
		send_mail(
			'Pong game email checking',
			f'Click the link to activate your account : {verification_link}',
			from_mail,
			[user_email],
			fail_silently=False,
        )
		return Response({"message": "Send verification mail successfully !"}, status=status.HTTP_200_OK)
	except Exception as e:
		return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def email_verified(request):
	token = request.data.get('token')
	print(token)
	if token and token == "true_email":
		return Response({"message": "Email has been verified, user account is now activated"}, status=status.HTTP_200_OK)
	return Response({"message": "Email verification failed."}, status=status.HTTP_300_MULTIPLE_CHOICES)




	# def create_activation_link(self, user):
	# 	token = "token_de_verification"
	# 	return reverse('activation_view', kwargs={'token': token}, request=self.request)

	# def send_activation_email(self, email, activation_link):
	# 	subject = 'Activer votre compte'
	# 	message = f'Cliquez sur le lien suivant pour activer votre compte : {activation_link}'
	# 	from_email = 'ponggame@test.com'
	# 	try:
	# 		send_mail(subject, message, from_email, [email])
	# 	except Exception as e:
	# 		print(f"Erreur d'envoi d'email: {str(e)}")

	# def perform_create(self, serializer):
	# 	activation_link = create_
	# 	serializer.save()