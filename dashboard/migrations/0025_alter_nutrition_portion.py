# Generated by Django 5.0.6 on 2024-07-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_alter_activity_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='portion',
            field=models.IntegerField(),
        ),
    ]
