# Generated by Django 5.0.6 on 2024-07-05 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_nutrition_carbs_nutrition_fats_nutrition_protein_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutrition',
            old_name='serving',
            new_name='portion',
        ),
    ]
