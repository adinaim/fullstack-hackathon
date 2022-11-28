from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class UserProfile(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birthday = models.DateField()
    cashaback = models.PositiveIntegerField(default=3)
    collected_sum = models.PositiveIntegerField(verbose_name='Собранная сумма')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name,' ',  self.last_name

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'