# Generated by Django 3.2.7 on 2021-09-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0011_merchmanunited'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchBarcelona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='real/')),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(null=True)),
                ('size', models.CharField(choices=[('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl'), ('xxl', 'xxl')], default='M', max_length=30)),
                ('description', models.TextField(default='no description', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
