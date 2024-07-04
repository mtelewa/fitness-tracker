# Generated by Django 5.0.6 on 2024-07-04 10:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_activity_calories_burnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='distance',
            field=models.FloatField(blank=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(1)]),
        ),
    ]