# Generated by Django 3.0.13 on 2021-05-10 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='users_liked',
            new_name='users_like',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%y/%d'),
        ),
    ]
