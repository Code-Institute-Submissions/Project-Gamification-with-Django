# Generated by Django 2.0.4 on 2018-06-04 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity_donation', '0006_auto_20180530_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'verbose_name': 'User Donation', 'verbose_name_plural': 'User Donations'},
        ),
    ]
