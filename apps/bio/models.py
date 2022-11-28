from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_profile',
        primary_key=True
    )
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    cashaback = models.PositiveIntegerField(default=3)
    collected_sum = models.PositiveIntegerField(verbose_name='Собранная сумма')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    collected_sum = models.PositiveIntegerField(verbose_name='Собранная сумма', default=0)


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'