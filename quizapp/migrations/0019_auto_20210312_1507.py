# Generated by Django 3.1.6 on 2021-03-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0018_auto_20210312_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='profile',
            field=models.ImageField(blank=True, default='img/default.jpg', null=True, upload_to='profile_pic'),
        ),
    ]
