# Generated by Django 4.0.6 on 2022-12-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_tutorialimage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_link',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
