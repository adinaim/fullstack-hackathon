from django.db import models
from django.contrib.auth import get_user_model

from apps.business.models import Tour

User = get_user_model()

class TourPurchase(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Ожидается'),
        ('finished', 'Пройден')
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        related_name='orders'
    )
    tour = models.ManyToManyField(
        to=Tour,
        through='TourItems',
    )
    order_id = models.CharField(max_length=58, blank=True)
    people_num = models.PositiveIntegerField()
    total_sum = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='pending')
    # address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ №{self.order_id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.order_id:
            self.order_id = str(self.user.username) + '-' + (str(self.created_at))[9:16].replace(':', '-').replace(' ', '-')
        return self.order_id

    class Meta:
        verbose_name = 'Покупка тура'
        verbose_name_plural = 'Покупки туров'


class TourItems(models.Model):
    order = models.ForeignKey(
        to=TourPurchase,
        on_delete=models.RESTRICT,  # какие on delete еще есть
        related_name='items'
    )
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.RESTRICT,  # какие on delete еще есть
        related_name='items'
    )
    people_num = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Объект корзины'
        verbose_name_plural = 'Объекты корзины'