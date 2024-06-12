from django.db import models

# Create your models here.

class Activity(models.Model):
    activity_type = models.CharField(max_length=200, unique=True)
    user = models.CharField(max_length=200, unique=True)
    distance = models.FloatField()
    duration = models.FloatField()
    registered_on = models.DateTimeField(auto_now_add=True)
    calories_burnt = models.IntegerField()

    class Meta:
        """
        The ordering option adds metadata to the model about
        the default order in which the list of activities is displayed
        """
        ordering = ["registered_on"]