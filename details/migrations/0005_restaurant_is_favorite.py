# Generated by Django 4.1 on 2024-09-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_rename_latitude_restaurant_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
