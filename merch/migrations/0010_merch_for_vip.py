# Generated by Django 3.2.7 on 2021-09-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0009_merchreal_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='merch',
            name='for_vip',
            field=models.BooleanField(default=0),
        ),
    ]
