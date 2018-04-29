# Generated by Django 2.0.4 on 2018-04-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('project_manager', models.CharField(default='', max_length=254)),
                ('budget', models.DecimalField(decimal_places=0, max_digits=6)),
                ('project_plan', models.ImageField(upload_to='images')),
            ],
        ),
    ]
