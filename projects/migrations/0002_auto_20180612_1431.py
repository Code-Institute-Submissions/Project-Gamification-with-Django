# Generated by Django 2.0.4 on 2018-06-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commitskill',
            name='skill',
            field=models.CharField(default='html', max_length=254),
        ),
        migrations.AlterField(
            model_name='gamificationadvice',
            name='name',
            field=models.CharField(default='advice', max_length=254),
        ),
    ]
