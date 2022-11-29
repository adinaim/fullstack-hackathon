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
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название компании')),
                ('image', models.ImageField(upload_to='media/business_profile_images')),
                ('desc', models.CharField(max_length=200, verbose_name='О компании')),
                ('phone', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=150, verbose_name='Электронная почта')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='Адресс')),
                ('slug', models.SlugField(blank=True, max_length=200, primary_key=True, serialize=False)),
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
            name='BusinessImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/tour_image')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus_images', to='business.businessprofile')),
            ],
        ),
    ]
