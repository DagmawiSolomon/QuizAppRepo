# Generated by Django 3.1.6 on 2021-03-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0013_auto_20210310_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='profile',
            field=models.ImageField(blank=True, default='/media/default.jpg', null=True, upload_to='profile_pic'),
        ),
    ]
