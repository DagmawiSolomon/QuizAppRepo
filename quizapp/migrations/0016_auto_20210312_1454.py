# Generated by Django 3.1.6 on 2021-03-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0015_auto_20210312_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]