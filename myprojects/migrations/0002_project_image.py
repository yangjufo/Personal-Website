# Generated by Django 2.1.4 on 2018-12-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.CharField(default='img/profile.jpg', max_length=100),
        ),
    ]