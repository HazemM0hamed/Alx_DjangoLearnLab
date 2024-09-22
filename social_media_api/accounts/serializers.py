from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add this line to include password field
    password = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'bio']
    
    def create(self, validated_data):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],  # Ensure password is included here
            bio=validated_data.get('bio', '')
        )
        Token.objects.create(user=user)
        return user
        get_user_model().objects.create_user

class CustomUserSerializer(serializers.ModelSerializer):
    following = serializers.StringRelatedField(many=True, read_only=True)
    followers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'following', 'followers']
