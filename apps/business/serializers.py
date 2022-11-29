from email.policy import default
from rest_framework import serializers

from .models import (
    BusinessProfile,
    Guide,
    Tour,
    TourImage,
)
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

    # def to_representation(self, instance):
    #     rep =  super().to_representation(instance)
    #     rep['guide'] = GuideListSeriaizer(
    #         instance.guides.all(), many=True
    #     )
    #     return rep
    #     # rep['tour'] = TourListSerializer(
    #     #     instance.title.all(), many=True
    #     # )



class BusinessProfileListSerializer(serializers.ModelSerializer):

     class Meta:
        model = BusinessProfile
        fields = ['title', 'phone', 'email', 'address']


class GuideCreateSerializer(serializers.ModelSerializer):

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
        fields = ['first_name', 'last_name', 'company_name']


class TourCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

    title = serializers.CharField(max_length=150)
    image = serializers.ImageField()
    tour_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        # blank=True
    )
    guide = serializers.CharField(max_length=100)
    place = serializers.CharField(max_length=150)
    date = serializers.DateField()
    price = serializers.IntegerField()
    people_count = serializers.IntegerField()
    desc = serializers.CharField(max_length=150)
    level = serializers.CharField(max_length=9)
    number_of_days = serializers.IntegerField()

    def create(self, validated_data):
        # tour = Tour.objects.create(**validated_data)
        avatar_carousel = validated_data.pop('tour_image_carousel')
        tour = Tour.objects.create(**validated_data)
        images = []
        for image in avatar_carousel:
            images.append(TourImage(tour=tour, image=image))
        TourImage.objects.bulk_create(images)
        return tour

    
class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['title', 'image', 'place', 'date', 'level', 'price', 'number_of_days']
