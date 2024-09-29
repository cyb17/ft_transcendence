from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

class CustomUser(AbstractUser):

	nickname = models.CharField(max_length=30)
	email = models.EmailField(unique=True, blank=False, null=False)
	avatar = models.URLField(blank=True, null=True)
	friends = models.ManyToManyField('self', related_name='friend_set', symmetrical=False, blank=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'nickname']

	def __str__(self):
		return self.username

	def get_full_name(self):
		return self.nickname

	# def has_perm(self, perm, obj=None):
	# 	return True

	# def has_module_perms(self, perm, obj=None):
	# 	return True

	# @property
	# def is_admin(self):
	# 	return self.is_staff

