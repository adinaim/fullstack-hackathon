# Generated by Django 4.1.3 on 2022-12-03 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_guide_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='company_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='guides', to='business.businessprofile', verbose_name='Компания'),
        ),
    ]