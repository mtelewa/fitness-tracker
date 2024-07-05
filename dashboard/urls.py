from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('profile/', views.profile_details, name='profile'),
    path('activity/', views.activity_history, name='activity'),
    path('nutrition/', views.nutrition_history, name='nutrition'),
    path('calendar/', views.calendar, name='calendar'),
    path('nutrition_delete/', views.entry_delete, name='nutrition_delete'),
    path('activity_delete/', views.entry_delete, name='activity_delete'),
    path('profile_delete/', views.entry_delete, name='profile_delete'), 
]