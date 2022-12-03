# Generated by Django 4.1.3 on 2022-12-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tutorialcategory_tutorial_tutorial_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_image',
            field=models.ImageField(default=1, upload_to='files/covers'),
            preserve_default=False,
        ),
    ]
