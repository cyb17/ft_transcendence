from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('', views.ListUsers.as_view(), name='list'),
	path('create/', views.CreateUser.as_view(), name='create'),
	path('<int:pk>/', views.UserOperations.as_view(), name='operations_RUD'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]