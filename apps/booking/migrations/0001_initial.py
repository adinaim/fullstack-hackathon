# Generated by Django 4.1.3 on 2022-11-29 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TourItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_num', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Объект корзины',
                'verbose_name_plural': 'Объекты корзины',
            },
        ),
        migrations.CreateModel(
            name='TourPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=58)),
                ('people_num', models.PositiveIntegerField()),
                ('total_sum', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('status', models.CharField(choices=[('pending', 'Ожидается'), ('finished', 'Пройден')], default='pending', max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tour', models.ManyToManyField(through='booking.TourItems', to='business.tour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Покупка тура',
                'verbose_name_plural': 'Покупки туров',
            },
        ),
        migrations.AddField(
            model_name='touritems',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='items', to='booking.tourpurchase'),
        ),
        migrations.AddField(
            model_name='touritems',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='items', to='business.tour'),
        ),
    ]
