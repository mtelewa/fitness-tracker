# Generated by Django 5.0.6 on 2024-06-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_activity_calories_burnt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(default='1990-09-07'),
            preserve_default=False,
        ),
    ]