# Generated by Django 4.1.3 on 2022-11-27 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 27, 10, 52, 37, 633777), verbose_name='date published'),
        ),
    ]
