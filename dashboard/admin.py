from django.contrib import admin
from .models import *


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'duration', 'calories_burnt',
                    'activity_on',)
    ordering = ('-activity_on',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('weight', 'height', 'birthdate', 'updated_on',)
    ordering = ('-updated_on',)


@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ('food_item', 'calories_intake',)
    ordering = ('-nutrition_on',)
