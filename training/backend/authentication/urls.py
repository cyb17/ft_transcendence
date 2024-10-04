from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('', views.ListUsers.as_view(), name='list'),
	path('create/', views.CreateUser.as_view(), name='create'),
	path('<int:pk>/', views.UserOperations.as_view(), name='operations_RUD'),
	path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('logout/', views.user_logout, name='logout'),
]