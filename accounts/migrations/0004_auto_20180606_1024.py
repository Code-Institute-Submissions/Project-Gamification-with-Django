# Generated by Django 2.0.4 on 2018-06-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_personalityquestion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonalityQuestion',
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='personality',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
    ]