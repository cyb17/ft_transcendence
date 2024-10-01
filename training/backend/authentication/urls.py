from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('list/', views.ListUsers.as_view(), name='liste_users'),
	path('create/', views.CreateUser.as_view(), name='create_user'),
	path('delete/<int:pk>/', views.UserOperations.as_view(), name='delete_user'),
	path('update/<int:pk>/', views.UserOperations.as_view(), name='update_user'),
	path('retrieve/<int:pk>/', views.UserOperations.as_view(), name='retrieve_user'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]