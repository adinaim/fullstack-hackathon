from rest_framework import serializers

from .models import Tour, TourImage


class TourCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = '__all__'

    tour_image_carousel = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
    )


    def create(self, validated_data):
        avatar_carousel = validated_data.pop('tour_image_carousel')
        tour = Tour.objects.create(**validated_data)
        images = []
        for image in avatar_carousel:
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

    
class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['title', 'image', 'place', 'level', 'number_of_days', 'price']


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImage
        fields = 'image'