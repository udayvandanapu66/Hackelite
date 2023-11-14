# Generated by Django 4.2.6 on 2023-10-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelXpressDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FX_name', models.CharField(max_length=100)),
                ('FX_license_number', models.CharField(max_length=20)),
                ('FX_phone_number', models.CharField(max_length=100)),
                ('FX_email', models.EmailField(max_length=254)),
                ('FX_availability', models.BooleanField(default=True)),
            ],
        ),
    ]
