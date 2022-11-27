from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import UserProfile


User = get_user_model()


class UserProfileCreateSerializer(serializers.Serializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=40)
    
    def create(self, validated_data):
        # return super().create(validated_data)
        profile = UserProfile.objects.create(**validated_data)
        return profile

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserProfile
