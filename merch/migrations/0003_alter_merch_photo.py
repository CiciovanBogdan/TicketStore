# Generated by Django 3.2.7 on 2021-09-09 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0002_merch_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merch',
            name='photo',
            field=models.CharField(default='https://www.freeiconspng.com/uploads/no-image-icon-4.png', help_text='image url', max_length=255),
        ),
    ]