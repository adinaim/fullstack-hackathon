from email.policy import default
from rest_framework import serializers

from .models import BusinessProfile
from apps.account.utils import normalize_phone



class BusinessProfileCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username',
        default=serializers.CurrentUserDefault()
    )
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()#upload_to='media/business_profile_images')
    desc = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=13)
    email = serializers.EmailField(max_length=150)
    address = serializers.CharField(max_length=150)


    class Meta:
        model = BusinessProfile
        fields = '__all__'

    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Invalid phone format!')
        return phone  

    def create(self, validated_data):
        profile = BusinessProfile.objects.create(**validated_data)
        return profile


class BusinessProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessProfile
        fields = '__all__'


class BusinessProfileListSerializer(serializers.ModelSerializer):

     class Meta:
        model = BusinessProfile
        fields = ['title', 'phone', 'email', 'address']