from . import views
from django.urls import path


urlpatterns = [
    path('nutrition_guide/', views.index, name='nutrition_guide'),
]