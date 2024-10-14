from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from .validators import validate_alnum

class User(AbstractUser):
	username = models.CharField(
		max_length=15,
		unique=True,
		validators=[MinLengthValidator(3), validate_alnum]
		)
	nickname = models.CharField(max_length=30, blank=True, null=False)
	email = models.EmailField(unique=True, blank=False, null=False)
	is_active = models.BooleanField(default=False)
	avatar = models.URLField(blank=True, null=True, default='default_avatar_url')
	friends = models.ManyToManyField('self', related_name='friend_set', symmetrical=False, blank=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'nickname']

	def __str__(self):
		return self.username
