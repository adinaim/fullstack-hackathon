from email.policy import default
from rest_framework import serializers

from .models import (
    BusinessProfile,
    Guide,
    BusinessImage
)
from apps.account.utils import normalize_phone



class BusinessProfileCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username',
        default=serializers.CurrentUserDefault()
    )
    # title = serializers.CharField(max_length=100)
    # image = serializers.ImageField()#upload_to='media/business_profile_images')
    # desc = serializers.CharField(max_length=200)
    # phone = serializers.CharField(max_length=13)
    # email = serializers.EmailField(max_length=150)
    # address = serializers.CharField(max_length=150)

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
      

class BusinessImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessImage
        fields = 'image',


class BusinessProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessProfile
        fields = '__all__'

    def to_representation(self, instance):          # не показывает
        rep =  super().to_representation(instance)
        rep['guides'] = GuideListSeriaizer(
            instance.guides.all(), many=True
        ).data
        return rep
        # rep['tour'] = TourListSerializer(
        #     instance.title.all(), many=True
        # ).data


class BusinessProfileListSerializer(serializers.ModelSerializer):

     class Meta:
        model = BusinessProfile
        fields = ['title', 'phone', 'email', 'address']


class GuideCreateSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(
    #     source='user.username',
    #     default=serializers.CurrentUserDefault()
    # )

    class Meta:
        model = Guide 
        fields = '__all__'

    # company_name = serializers.ReadOnlyField(
    #     source='company_name.slug'
    # )

    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Invalid phone format!')
        return phone  

    def create(self, validated_data):
        guide = Guide.objects.create(**validated_data)
        return guide


class GuideSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'


class GuideListSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ['first_name', 'last_name']