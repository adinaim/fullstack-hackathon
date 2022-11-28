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
      
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['guide'] = GuideListSerializer(
            instance.guides.all(), many=True
        )
        return rep
        # rep['tour'] = TourListSerializer(
        #     instance.title.all(), many=True
        # )


class BusinessProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessProfile
        fields = '__all__'


class BusinessProfileListSerializer(serializers.ModelSerializer):

     class Meta:
        model = BusinessProfile
        fields = ['title', 'phone', 'email', 'address']




class GuideCreateSerializer(serializers.ModelSerializer):
    # company_name = serializers.ReadOnlyField(
    #     source='company_name.title'
    # )
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    class Meta:
        model = Guide
        fields = '__all__'

    # def create(self, validated_data):
    #     # return super().create(validated_data)
    #     guide = Guide.objects.create(**validated_data)
    #     return guide


class GuideListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'


class TourCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    company_name = serializers.CharField(max_length=150)
    guide = serializers.CharField(max_length=150)
    image = serializers.ImageField()
    image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )
    place = serializers.CharField(max_length=100)
    date = serializers.DateField()
    price = serializers.IntegerField()
    people_count = serializers.CharField(max_length=2)
    desc = serializers.CharField(max_length=150)
    number_of_days = serializers.IntegerField()
    level = serializers.CharField(max_length=8)

    class Meta:
        model = Tour
        fields = '__all__'

    def create(self, validated_data):
        tour = Tour.objects.create(**validated_data)
        image_carousel = validated_data.pop('image_carousel')
        images = []
        for image in image_carousel:
            images.append(TourImage(tour=tour, image=image))
        TourImage.objects.bulk_create(images)
        return tour

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = TourImageSerializer(
            instance.tour_images.all(),
            many=True
        ).data 
        return rep


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = 'image'


class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['title', 'place', 'date', 'level']