# Generated by Django 3.2.6 on 2021-09-01 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitality', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitality',
            name='price',
            field=models.IntegerField(help_text='price in euro'),
        ),
    ]
