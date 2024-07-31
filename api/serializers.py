from rest_framework import serializers
from .models import User, Chat

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'tokens']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['user', 'message', 'response', 'timestamp']
