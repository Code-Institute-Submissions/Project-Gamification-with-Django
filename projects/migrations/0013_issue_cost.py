# Generated by Django 2.0.4 on 2018-05-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_issue_proposed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='cost',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
    ]
