# Generated by Django 2.1.7 on 2019-02-27 19:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SpeechToText', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Token',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
