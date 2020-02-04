# Generated by Django 2.2.6 on 2020-02-04 00:17

from django.db import migrations, models
import django.db.models.deletion
import skiing.models


class Migration(migrations.Migration):

    dependencies = [
        ('skiing', '0017_auto_20191230_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skiday',
            name='resort',
            field=models.ForeignKey(blank=True, default=skiing.models.get_default_resort, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skidays', to='skiing.Resort'),
        ),
    ]
