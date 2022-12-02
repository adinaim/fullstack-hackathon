from django.db import models
from slugify import slugify
from apps.business.models import BusinessProfile, Guide


class Tour(models.Model):
    LEVEL_CHOICES = (
        ('easy', 'легкий'),
        ('medium', 'средний'),
        ('hard', 'сложный')
    )

    title = models.CharField(max_length=100, verbose_name='Название тура')
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)

    company_name = models.ForeignKey(
        to=BusinessProfile,
        on_delete=models.CASCADE,
        verbose_name='Компания',
        # related_name='tour'
    )
    guide = models.ForeignKey(
        to=Guide,
        on_delete=models.CASCADE,
        verbose_name='Гид',
        related_name='tour'
    )
    image = models.ImageField(upload_to='media/tour_image')
    place = models.CharField(max_length=100, verbose_name='Место')
    desc = models.CharField(max_length=150)
    number_of_days = models.PositiveIntegerField()
    level = models.CharField(max_length=8, choices=LEVEL_CHOICES, verbose_name='Уровень')
    price = models.PositiveSmallIntegerField(verbose_name='Цена в национальной валюте')
    date = models.DateField()
    people_count = models.PositiveSmallIntegerField(verbose_name='Количество мест на тур')


    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.title)
        # if not self.price_usd:
        #     self.price_usd = round(self.price_som / 84, 1)
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class TourImage(models.Model):
    image = models.ImageField(upload_to='media/tour_image')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='tour_images',
    )
