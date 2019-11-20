# Generated by Django 2.2.6 on 2019-10-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skiing', '0007_auto_20191020_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resort',
            old_name='acres',
            new_name='skiable_acres',
        ),
        migrations.AddField(
            model_name='resort',
            name='base_elevation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resort',
            name='longest_run',
            field=models.IntegerField(default=0),
        ),
    ]
