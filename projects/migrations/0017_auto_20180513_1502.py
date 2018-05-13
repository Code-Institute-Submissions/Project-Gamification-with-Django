# Generated by Django 2.0.4 on 2018-05-13 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_projectskillset'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequiredSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
                ('html', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
                ('js', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
                ('css', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
                ('mongodb', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
                ('mysql', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='projectskillset',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectskillset',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='project',
            name='issues',
        ),
        migrations.DeleteModel(
            name='ProjectSkillSet',
        ),
        migrations.AddField(
            model_name='requiredskills',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
