# Generated by Django 3.2.7 on 2021-09-23 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitality', '0011_auto_20210923_1345'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hospitality',
        ),
        migrations.DeleteModel(
            name='HospitalityReal',
        ),
    ]
