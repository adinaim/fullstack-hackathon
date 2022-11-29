# Generated by Django 4.1.3 on 2022-11-29 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название компании')),
                ('image', models.ImageField(upload_to='media/business_profile_images')),
                ('desc', models.CharField(max_length=200, verbose_name='О компании')),
                ('phone', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=150, verbose_name='Электронная почта')),
                ('address', models.CharField(max_length=150, verbose_name='Адресс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль компании',
                'verbose_name_plural': 'Профили компаний',
            },
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('slug', models.SlugField(blank=True, max_length=200, primary_key=True, serialize=False)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guides', to='business.businessprofile', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Гид',
                'verbose_name_plural': 'Гиды',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('title', models.CharField(max_length=100, verbose_name='Название тура')),
                ('slug', models.SlugField(blank=True, max_length=120, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='media/tour_image')),
                ('place', models.CharField(max_length=100, verbose_name='Место')),
                ('price_som', models.PositiveSmallIntegerField(verbose_name='Цена в национальной валюте')),
                ('price_usd', models.PositiveSmallIntegerField(blank=True, verbose_name='Цена в USD')),
                ('desc', models.CharField(max_length=150)),
                ('number_of_days', models.PositiveIntegerField()),
                ('level', models.CharField(choices=[('easy', 'легкий'), ('medium', 'средний'), ('hard', 'сложный')], max_length=8, verbose_name='Уровень')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.businessprofile', verbose_name='Компания')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.guide', verbose_name='Гид')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/tour_image')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_images', to='business.tour')),
            ],
        ),
        migrations.CreateModel(
            name='ConcreteTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('people_count', models.PositiveSmallIntegerField(verbose_name='Количество мест на тур')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.tour', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Конкретный тур',
                'verbose_name_plural': 'Конкретные туры',
            },
        ),
        migrations.CreateModel(
            name='BusinessImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/tour_image')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus_images', to='business.businessprofile')),
            ],
        ),
    ]
