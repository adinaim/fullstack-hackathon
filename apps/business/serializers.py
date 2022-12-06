from email.policy import default
from urllib import request
from rest_framework import serializers
from django.db.models import Avg
from .models import (
    BusinessProfile,
    Guide,
    BusinessImage
)
from django.contrib.auth import get_user_model
from apps.account.utils import normalize_phone
from apps.bio.models import UserProfile 
from apps.review.serializers import GuideRatingSerializer, RatingSerializer

User = get_user_model()

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

    # def validate(self, attrs):
    #     user = self.context.get('request').user
    #     print(request)
    #     print(self.context)

    #     profile = UserProfile.objects.filter(user=user).first()
    #     if profile:
    #         raise serializers.ValidationError('У вас уже существует профиль!')
    #     return attrs

      

class BusinessImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessImage
        fields = 'image',


class BusinessProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = BusinessProfile
        fields = '__all__'

    def to_representation(self, instance):          # не показывает
        rep =  super().to_representation(instance)
        rep['guides'] = GuideListSerializer(
            instance.comp.all(), many=True
        ).data
        return rep
        # rep['tour'] = TourListSerializer(
        #     instance.title.all(), many=True
        # ).data


class BusinessProfileListSerializer(serializers.ModelSerializer):

     class Meta:
        model = BusinessProfile
        fields = ['title', 'phone', 'email', 'address']


class GuideSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    company_name = serializers.ReadOnlyField(source='company_name.title')

    class Meta:
        model = Guide 
        fields = '__all__'

    def create(self, validated_data):
        guide = Guide.objects.create(**validated_data)
        return guide

    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        attrs['company_name'] = user.profile
        return attrs

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     # rating = instance.rating.aggregate(Avg('rating'))['rating__avg']
    #     # if rating:
    #     #     rep['rating'] = round(rating,1)
    #     # else:
    #     #     rep['rating'] = 0.0
    #     rep['rating'] = RatingSerializer(
    #         instance=instance.rating.all(),
    #         many=True
    #     ).data


class GuideListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        exclude = ['slug', 'company_name']

        # return request.user.is_authenticated and request.user == obj.user
        # AttributeError: 'Guide' object has no attribute 'user'

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rating = instance.rating_guide.aggregate(Avg('rating'))['rating__avg']
    #     if rating:
    #         rep['rating'] = round(rating,1)
    #     else:
    #         rep['rating'] = 0.0
