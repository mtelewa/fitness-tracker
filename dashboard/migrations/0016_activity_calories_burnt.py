# Generated by Django 5.0.6 on 2024-07-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_alter_activity_distance_alter_activity_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='calories_burnt',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]