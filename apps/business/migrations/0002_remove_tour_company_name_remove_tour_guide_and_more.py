# Generated by Django 4.1.3 on 2022-11-29 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='guide',
        ),
        migrations.RemoveField(
            model_name='tourimage',
            name='tour',
        ),
        migrations.DeleteModel(
            name='ConcreteTour',
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
        migrations.DeleteModel(
            name='TourImage',
        ),
    ]