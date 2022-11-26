from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BusinessProfile(models.Model):

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    title = models.CharField(max_length=100, verbose_name='Название компании', unique=True)
    image = models.ImageField(upload_to='media/business_profile_images')
    desc = models.CharField(max_length=200, verbose_name='О компании')
    phone = models.CharField(max_length=13, verbose_name='Номер телефона')
    email = models.EmailField(max_length=150, verbose_name='Электронная почта')
    address = models.CharField(max_length=150, verbose_name='Адресс')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Профиль компании'
        verbose_name_plural = 'Профили компаний'



      