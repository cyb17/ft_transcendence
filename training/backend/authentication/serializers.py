from rest_framework import serializers
from .models import CustomUser

# class FriendSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = CustomUser
# 		fields = ['id', 'username']
# 	friends = FriendSerializer(many=True, required=False)

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ['id', 'username', 'nickname', 'email', 'password', 'avatar', 'friends', 'is_staff', 'is_active', 'date_joined']
		extra_kwargs = { 
			'id': {'read_only': True},
			'friends': {'read_only': True},
			'is_staff': {'read_only': True},
			'is_active': {'read_only': True},
			'date_joined': {'read_only': True},
			'password': {'write_only': True},
			}

	# save() par defaut ne hash pas le MDP user, donc redefinition ici.
	def save(self, **kwargs):
		user = super().save(**kwargs)
		user.set_password(user.password)
		user.save()
		return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)