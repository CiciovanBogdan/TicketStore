# Generated by Django 3.2.7 on 2021-09-20 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0014_fixturebarcelona_fixturemanunited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixturebarcelona',
            name='price',
        ),
        migrations.RemoveField(
            model_name='fixturemanunited',
            name='price',
        ),
    ]
