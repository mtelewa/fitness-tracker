# Generated by Django 5.0.6 on 2024-07-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_nutrition_calories_intake_delete_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrition',
            name='carbs',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutrition',
            name='fats',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutrition',
            name='protein',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutrition',
            name='serving',
            field=models.CharField(default='50 g', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='food_item',
            field=models.CharField(max_length=200),
        ),
    ]