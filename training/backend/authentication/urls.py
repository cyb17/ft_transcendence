from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
	path('', include(router.urls)),
	path('login/', views.CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', views.CookieTokenRefreshView.as_view(), name='token_refresh'),
	path('logout/', views.user_logout, name='logout'),
	path('sendMail/', views.send_mymail),
]