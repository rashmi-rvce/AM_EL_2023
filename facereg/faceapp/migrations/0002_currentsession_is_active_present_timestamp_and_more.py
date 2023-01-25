# Generated by Django 4.0 on 2022-01-22 18:16

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('faceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentsession',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='present',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.localtime),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currentsession',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterUniqueTogether(
            name='present',
            unique_together={('session', 'student')},
        ),
    ]