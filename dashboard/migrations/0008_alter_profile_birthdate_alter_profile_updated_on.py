# Generated by Django 5.0.6 on 2024-06-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_profile_height_alter_profile_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]