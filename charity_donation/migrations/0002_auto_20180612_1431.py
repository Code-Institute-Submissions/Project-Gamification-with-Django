# Generated by Django 2.0.4 on 2018-06-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_donation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.CharField(default='Donor', max_length=50),
        ),
    ]
