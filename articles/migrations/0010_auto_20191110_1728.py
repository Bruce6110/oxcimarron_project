# Generated by Django 2.2.6 on 2019-11-10 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_article_t2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='imageTest',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
