from . import views
from django.urls import path


urlpatterns = [
    path('activity/', views.index, name='activity'),
]