
from rest_framework import serializers
from .models import FriendRequest
from django.contrib.auth.models import User
from django.db import models

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'status', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FriendListSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'friends']

    def get_friends(self, obj):
        # Retrieve all accepted friend requests involving the user
        accepted_requests = FriendRequest.objects.filter(
            (models.Q(from_user=obj) | models.Q(to_user=obj)),
            status='accepted'
        )
        
        friends = set()  # Use set to avoid duplicates
        for req in accepted_requests:
            if req.from_user == obj:
                friends.add(req.to_user)
            else:
                friends.add(req.from_user)
                
        return UserSerializer(list(friends), many=True).data
