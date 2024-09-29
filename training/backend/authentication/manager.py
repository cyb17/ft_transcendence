from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

	def created_user(self, username, email, password):
		if not email:
			raise TypeError(_('No email provided'))
		if not password:
			raise TypeError(_('No password provided'))
		user = self.model(username=username, email=self.normalize_email(email))
		user.set_password(password)
		user.clean_fields()
		user.save()
		return user
