# Generated by Django 4.1.3 on 2022-12-04 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour', '0001_initial'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_tour', to='tour.concretetour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]