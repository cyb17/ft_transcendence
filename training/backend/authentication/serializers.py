from rest_framework import serializers
from .models import CustomUser

class FriendSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ['id', 'username']

class CustomUserSerializer(serializers.ModelSerializer):
	friends = FriendSerializer(many=True, required=False)

	class Meta:
		model = CustomUser
		fields = ['id', 'username', 'nickname', 'email', 'password', 'avatar', 'friends', 'is_staff', 'is_active', 'date_joined']
		
		# permet de recevoir ce donnees mais ne l'affichera pas dans la reponse retournee
		extra_kwargs = { 'password': {'write_only': True} }

	# save() par defaut ne hash pas le MDP user, donc redefinition ici.
	def save(self, **kwargs):
		user = super().save(**kwargs)
		user.set_password(user.password)
		user.save()
		return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)