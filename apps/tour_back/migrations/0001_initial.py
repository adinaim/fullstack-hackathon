# Generated by Django 4.1.3 on 2022-12-01 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0003_guide_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('title', models.CharField(max_length=100, verbose_name='Название тура')),
                ('slug', models.SlugField(blank=True, max_length=120, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='media/tour_image')),
                ('place', models.CharField(max_length=100, verbose_name='Место')),
                ('desc', models.CharField(max_length=150)),
                ('number_of_days', models.PositiveIntegerField()),
                ('level', models.CharField(choices=[('easy', 'легкий'), ('medium', 'средний'), ('hard', 'сложный')], max_length=8, verbose_name='Уровень')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='business.businessprofile', verbose_name='Компания')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_back', to='business.guide', verbose_name='Гид')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_images', to='tour_back.tour')),
            ],
        ),
        migrations.CreateModel(
            name='ConcreteTour',
            fields=[
                ('slug', models.SlugField(blank=True, max_length=120, primary_key=True, serialize=False)),
                ('price_som', models.PositiveSmallIntegerField(verbose_name='Цена в национальной валюте')),
                ('price_usd', models.PositiveSmallIntegerField(blank=True, verbose_name='Цена в USD')),
                ('date', models.DateField()),
                ('people_count', models.PositiveSmallIntegerField(verbose_name='Количество мест на тур')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concrete_tour', to='tour_back.tour', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Конкретный тур',
                'verbose_name_plural': 'Конкретные туры',
            },
        ),
    ]
