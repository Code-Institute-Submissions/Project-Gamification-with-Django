# Generated by Django 2.0.4 on 2018-06-06 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('charity_choice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User Donation',
                'verbose_name_plural': 'User Donations',
            },
        ),
        migrations.CreateModel(
            name='DonationLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity_choice.Charity')),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity_donation.Donation')),
            ],
        ),
    ]
