from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from .validators import validate_alnum
from .manager import UserManager

class User(AbstractUser):
	username = models.CharField(
		max_length=15,
		unique=True,
		validators=[MinLengthValidator(3), validate_alnum]
		)
	nickname = models.CharField(max_length=30)
	email = models.EmailField(unique=True)
	avatar = models.URLField(blank=True, null=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	created_at = models.DateTimeField(default=timezone.now)
	friends = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='friend_set')

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'nickname']

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, perm, obj=None):
		return True

	@property
	def is_admin(self):
		return self.is_staff

	def __str__(self):
		return self.username

	def get_full_name(self):
		return self.nickname