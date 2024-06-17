from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.

# admin.site.register(Activity)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('weight', 'height', )
