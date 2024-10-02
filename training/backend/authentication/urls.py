from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('users/', views.ListUsers.as_view(), name='users_list'),
	path('user/create/', views.CreateUser.as_view(), name='user_create'),
	path('user/login/', views.UserLogin.as_view(), name='user_login'),
	path('user/<int:pk>/', views.UserOperations.as_view(), name='user_RUD'),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]