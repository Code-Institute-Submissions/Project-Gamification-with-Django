# Generated by Django 2.0.4 on 2018-06-04 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AlterModelOptions(
            name='personality',
            options={'verbose_name': 'Personality Type', 'verbose_name_plural': 'Personality Types'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Company Position', 'verbose_name_plural': 'Company Positions'},
        ),
    ]