from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STARS = ((1, "Very Poor"), (2, "Poor"), (3, "Good"), (4, "Very Good"), (5, "Excellent"))

class Activity(models.Model):
    activity_type = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_activity"
        )
    distance = models.FloatField()
    duration = models.FloatField()
    activity_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        The ordering option adds metadata to the model about
        the default order in which the list of activities is displayed
        """
        ordering = ["activity_on"]


class Nutrition(models.Model):
    food_item = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_nutrition"
        )
    nutrition_on = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    message = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_review"
        )
    stars = models.IntegerField(choices=STARS, default=0)
    review = models.TextField()
    approved = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_profile"
        )
    height = models.IntegerField()
    weight = models.FloatField()
    weight_target = models.FloatField()
    profile_image = CloudinaryField('image', default="placeholder")
    updated_on = models.DateTimeField(auto_now_add=True)
    birthdate = models.DateField()

