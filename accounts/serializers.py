from .models import User
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'created_at']
        extra_kwargs = {"password": {"write_only":True}}

class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'created_at']