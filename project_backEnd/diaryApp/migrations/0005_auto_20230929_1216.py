# Generated by Django 2.2.12 on 2023-09-29 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryApp', '0004_auto_20230929_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_diary1',
            name='diary_contents',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='daily_diary1',
            name='diary_title',
            field=models.CharField(max_length=20),
        ),
    ]
