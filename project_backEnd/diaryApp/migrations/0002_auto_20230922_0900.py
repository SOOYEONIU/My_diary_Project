# Generated by Django 2.2.12 on 2023-09-22 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_diary1',
            name='diary_created_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
