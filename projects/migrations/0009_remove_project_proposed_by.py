# Generated by Django 2.0.4 on 2018-05-07 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_proposed_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='proposed_by',
        ),
    ]