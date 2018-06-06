# Generated by Django 2.0.4 on 2018-06-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('donation', models.DecimalField(decimal_places=0, default=5, max_digits=1)),
                ('image', models.ImageField(upload_to='donations')),
            ],
            options={
                'verbose_name': 'Proposed Charity',
                'verbose_name_plural': 'Proposed Charities',
            },
        ),
    ]
