# Generated by Django 2.0.2 on 2019-09-20 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skiing', '0002_auto_20190125_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skiday',
            name='year_written',
        ),
    ]
