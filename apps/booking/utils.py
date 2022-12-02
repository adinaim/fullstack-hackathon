from apps.bio.models import UserProfile
from .models import TourPurchase


def cashback(context, order, total_sum):
    user = context['request'].user
    profile = UserProfile.objects.filter(user=user)

    print('profile', str(profile))
    reward = int(profile.values('cashback')[0]['cashback'])
    print('reward', reward)
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



# отсюда вниз убрать в отдельный файл
    # reward = int(profile.values('cashback')[0]['cashback'])
    # order.total_sum = total_sum - total_sum*reward/100

    # collected_sum = int(profile.values('collected_sum')[0]['collected_sum'])
    # collected_sum += order.total_sum

    # profile.update(
    #     collected_sum=collected_sum)

    # check_cashback = int(profile.values('collected_sum')[0]['collected_sum']) 
    # if check_cashback >= 10000:
    #     profile.update(
    #         cashback=5)
    # if check_cashback >= 20000:
    #     profile.update(
    #         cashback=7)
    # if check_cashback >= 30000:
    #     profile.update(
    #         cashback=10)

    # user = self.context['request'].user
    #     profile = UserProfile.objects.filter(user=user)



    #     items = validated_data.pop('items')
    #     validated_data['user'] = self.context['request'].user
    #     order = super().create(validated_data) # Order.objects.create
    #     total_sum = 0
    #     orders_items = []
    #     for item in items:
    #         orders_items.append(OrderItems(
    #             order=order,
    #             book=item['book'],
    #             quantity=item['quantity']
    #         ))
    #         total_sum += item['book'].price * item['quantity']
    #     OrderItems.objects.bulk_create(orders_items, *args, **kwargs)

    #     reward = int(profile.values('cashback')[0]['cashback'])
    #     order.total_sum = total_sum - total_sum*reward/100

    #     collected_sum = int(profile.values('collected_sum')[0]['collected_sum'])
    #     collected_sum += order.total_sum

    #     profile.update(
    #         collected_sum=collected_sum)

    #     check_cashback = int(profile.values('collected_sum')[0]['collected_sum']) 
    #     if check_cashback >= 10000:
    #         profile.update(
    #             cashback=5)
    #     if check_cashback >= 20000:
    #         profile.update(
    #             cashback=7)
    #     if check_cashback >= 30000:
    #         profile.update(
    #             cashback=10)

    #     order.save()
    #     return order