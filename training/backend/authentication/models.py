from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

	nickname = models.CharField(max_length=30, blank=True, null=False)
	email = models.EmailField(unique=True, blank=False, null=False)
	avatar = models.URLField(blank=True, null=True, default='default_avatar_url')
	friends = models.ManyToManyField('self', related_name='friend_set', symmetrical=False, blank=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.username
