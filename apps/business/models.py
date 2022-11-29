from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
   
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Профиль компании'
        verbose_name_plural = 'Профили компаний'


class Guide(models.Model):
    company_name = models.ForeignKey(
        to=BusinessProfile,
        on_delete=models.CASCADE,
        verbose_name='Компания',
        related_name='guides'
    )
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    slug = models.SlugField(max_length=200, primary_key=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.first_name + '-' + self.last_name))
        return super().save(*args, **kwargs)
   
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Гид'
        verbose_name_plural = 'Гиды'


class Tour(models.Model):

    # PEOPLE_CHOICES = (
    #     (1, '1'),
    #     (2, '2'),
    #     (3, '3'),
    #     (4, '4'),
    #     (5, '5'),
    #     (6, '6'),
    #     (7, '8'),
    #     (9, '9'),
    #     (10, '10'),
    #     (11, '11'),
    #     (12, '12'),
    #     (13, '13'),
    #     (14, '14'),
    #     (15, '15'), 
    # )

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
        verbose_name='Компания'
    )
    guide = models.ForeignKey(
        to=Guide,
        on_delete=models.CASCADE,
        verbose_name='Гид'
    )
    image = models.ImageField(upload_to='media/tour_image')
    place = models.CharField(max_length=100, verbose_name='Место')
    # date = models.DateField(verbose_name='Дата')
    price_som = models.PositiveSmallIntegerField(verbose_name='Цена в национальной валюте')
    price_usd = models.PositiveSmallIntegerField(verbose_name='Цена в USD', blank=True)
    # people_count = models.CharField(max_length=2, choices=PEOPLE_CHOICES, verbose_name='Количество человек')
    desc = models.CharField(max_length=150)
    number_of_days = models.PositiveIntegerField()
    level = models.CharField(max_length=8, choices=LEVEL_CHOICES, verbose_name='Уровень')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.price_usd:
            self.price_usd = round(self.price_som / 84, 1)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class ConcreteTour(models.Model):
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        verbose_name='Тур'
    )
    date = models.DateField()
    people_count = models.PositiveSmallIntegerField(verbose_name='Количество мест на тур')

    class Meta:
        verbose_name = 'Конкретный тур'
        verbose_name_plural = 'Конкретные туры'


class TourImage(models.Model):
    image = models.ImageField(upload_to='media/tour_image')
    tour = models.ForeignKey(
        to=Tour,
        on_delete=models.CASCADE,
        related_name='tour_images',
    )


class BusinessImage(models.Model):
    image = models.ImageField(upload_to='media/tour_image')
    business = models.ForeignKey(
        to=BusinessProfile,
        on_delete=models.CASCADE,
        related_name='bus_images'
    )