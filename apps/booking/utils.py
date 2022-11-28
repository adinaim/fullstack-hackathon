from apps.bio.models import UserProfile
from .models import Order


def cashback(context, order, total_sum):
    user = context['request'].user
    profile = UserProfile.objects.filter(user=user)

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