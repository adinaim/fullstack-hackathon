# Generated by Django 4.1.3 on 2022-11-30 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touritems',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='booking.tourpurchase'),
        ),
        migrations.AlterField(
            model_name='touritems',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='business.guide'),
        ),
    ]
