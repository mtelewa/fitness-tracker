from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
from .models import Activity

# Register your models here.

# admin.site.register(Activity)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('calories_burnt',)
