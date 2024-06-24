from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('profile/', views.profile, name='profile'),
    path('calendar/', views.calendar, name='calendar'),
]