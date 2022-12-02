# Generated by Django 4.1.3 on 2022-12-01 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_guide_user'),
        ('tour_front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour', to='business.guide', verbose_name='Гид'),
        ),
        migrations.AlterField(
            model_name='tourimage',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour_images', to='tour_front.tour'),
        ),
    ]
