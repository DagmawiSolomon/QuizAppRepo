# Generated by Django 3.1.6 on 2021-03-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='result',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
