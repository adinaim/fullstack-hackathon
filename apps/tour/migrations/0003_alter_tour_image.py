# Generated by Django 4.1.3 on 2022-12-07 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_alter_concretetour_guide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/tour_image'),
        ),
    ]
