# Generated by Django 3.2.7 on 2021-09-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0007_merchreal'),
    ]

    operations = [
        migrations.AddField(
            model_name='merch',
            name='discount_price',
            field=models.IntegerField(null=True),
        ),
    ]