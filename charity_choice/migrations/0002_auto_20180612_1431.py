# Generated by Django 2.0.4 on 2018-06-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_choice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='name',
            field=models.CharField(default='Charity', max_length=254),
        ),
    ]
