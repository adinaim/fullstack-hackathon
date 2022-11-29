from rest_framework import serializers

from .models import (
    TourPurchase, 
    TourItems
)
from apps.bio.models import UserProfile
# from .tasks import send_detail_info

class TourItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourItems
        fields = ['order']


class TourPurchaseSerializer(serializers.ModelSerializer):
    items = TourItemsSerializer(many=True) 
     # проверять пвторизован ли user или анонимный

    class Meta:
        model = TourPurchase
        fields = ['order_id', 'created_at', 'total_sum', 'items']

    def create(self, validated_data, *args, **kwargs):
        user = self.context['request'].user
        profile = UserProfile.objects.filter(user=user)

        items = validated_data.pop('items')
        validated_data['user'] = self.context['request'].user
        order = super().create(validated_data) # Order.objects.create
        total_sum = 0
        orders_items = []
        for item in items:
            orders_items.append(TourItems(
                order=order,
                book=item['book'],
                quantity=item['quantity']
            ))
            total_sum += item['book'].price * item['quantity']
        TourItems.objects.bulk_create(orders_items, *args, **kwargs)
# отсюда вниз убрать в отдельный файл
        reward = int(profile.values('cashback')[0]['cashback'])
        order.total_sum = total_sum - total_sum*reward/100

        collected_sum = int(profile.values('collected_sum')[0]['collected_sum'])
        collected_sum += order.total_sum

        profile.update(
            collected_sum=collected_sum)

        check_cashback = int(profile.values('collected_sum')[0]['collected_sum']) 
        if check_cashback >= 10000:
            profile.update(
                cashback=5)
        if check_cashback >= 20000:
            profile.update(
                cashback=7)
        if check_cashback >= 30000:
            profile.update(
                cashback=10)

        order.save()
        profile.save()
        # send_detail_info()
        return order


class PurchaseHistorySerializer(serializers.ModelSerializer):

    # url = serializers.ReadOnlyField(source='order.get_absolute_url')
    # book = serializers.ReadOnlyField(source='order.book')
    
    class Meta:
        model = TourPurchase
        fields = ('order_id', 'total_sum', 'status', 'created_at', 'tour')

