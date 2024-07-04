from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('profile/', views.profile_details, name='profile'),
    path('activity/', views.activity_history, name='activity'),
    path('calendar/', views.calendar, name='calendar'),
]