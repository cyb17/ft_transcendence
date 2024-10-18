from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
	path('', include(router.urls)),
	path('login/', views.CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', views.CookieTokenRefreshView.as_view(), name='token_refresh'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	# path('verify-email/', views.send_mymail),
	# path('email-verified/', views.mail_verified),
]