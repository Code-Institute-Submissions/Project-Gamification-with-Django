# Generated by Django 2.0.4 on 2018-05-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180508_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]