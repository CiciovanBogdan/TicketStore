# Generated by Django 3.2.7 on 2022-01-03 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0018_merch_discount_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merch',
            name='discount_price',
        ),
    ]