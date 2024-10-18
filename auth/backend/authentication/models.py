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
	nickname = models.CharField(max_length=30, blank=True, null=True)
	email = models.EmailField(unique=True, blank=False, null=False)
	is_active = models.BooleanField(default=False)
	avatar = models.URLField(blank=True, null=True, default='https://thumbs.dreamstime.com/b/ic%C3%B4ne-de-profil-avatar-par-d%C3%A9faut-m%C3%A9dias-sociaux-utilisateur-vectoriel-social-portrait-176194876.jpg')
	friends = models.ManyToManyField('self', related_name='friendship', symmetrical=False, blank=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'nickname']

	def __str__(self):
		return self.username
