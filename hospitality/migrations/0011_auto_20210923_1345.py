# Generated by Django 3.2.7 on 2021-09-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitality', '0010_auto_20210921_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitality',
            name='for_barcelona',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hospitality',
            name='for_city',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hospitalityreal',
            name='for_real',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hospitalityreal',
            name='for_united',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]