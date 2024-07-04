from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

class Activity(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_activity"
        )
    activity_type = models.CharField(max_length=200)
    distance = models.FloatField(blank=True, null=True,
                validators=[
                MaxValueValidator(999),
                MinValueValidator(1)
                ])
    duration = models.FloatField(
                    validators=[
                    MaxValueValidator(999),
                    MinValueValidator(1)
                ])
    calories_burnt = models.IntegerField()
    activity_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        The ordering option adds metadata to the model about
        the default order in which the list of activities is displayed
        """
        ordering = ["activity_on"]


class Nutrition(models.Model):
    food_item = models.CharField(max_length=200)
    serving = models.CharField(max_length=200)
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fats = models.IntegerField()
    calories_intake = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_nutrition"
        )
    nutrition_on = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_profile"
        )
    height = models.FloatField(
        validators=[
            MaxValueValidator(999),
            MinValueValidator(1)
        ])
    weight = models.FloatField(null=True,
        validators=[
                MaxValueValidator(999),
                MinValueValidator(1)
        ])
    weight_target = models.FloatField(null=True,
            validators=[
                MaxValueValidator(999),
                MinValueValidator(1)
        ])
    profile_image = CloudinaryField('image', default="placeholder", null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    birthdate = models.DateField()

