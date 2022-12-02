from rest_framework import serializers

from .models import (
    TourPurchase, 
    TourItems
)
from apps.bio.models import UserProfile
from .utils import cashback
# from .tasks import send_detail_info

class TourItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourItems
        fields = ['tour', 'people_num']


class TourPurchaseSerializer(serializers.ModelSerializer):
    items = TourItemsSerializer(many=True) 
     # проверять пвторизован ли user или анонимный

    class Meta:
        model = TourPurchase
        fields = ['order_id', 'created_at', 'total_sum', 'items']

    def create(self, validated_data, *args, **kwargs):
        items = validated_data.pop('items')
        validated_data['user'] = self.context['request'].user
        order = super().create(validated_data) # Order.objects.create
        total_sum = 0
        orders_items = []
        for item in items:
            orders_items.append(TourItems(
                order=order,
                tour=item['tour'],
                people_num=item['people_num']
            ))
            total_sum += item['tour'].price_som * item['people_num']

        TourItems.objects.bulk_create(orders_items, *args, **kwargs)
        order.total_sum = total_sum

        if self.context['request'].user.is_authenticated:
            cashback(self.context, order, total_sum)

        order.save()
        # send_detail_info()
        return order


class PurchaseHistorySerializer(serializers.ModelSerializer):

    # url = serializers.ReadOnlyField(source='order.get_absolute_url')
    # book = serializers.ReadOnlyField(source='order.book')
    
    class Meta:
        model = TourPurchase
        fields = ('order_id', 'total_sum', 'status', 'created_at', 'tour')