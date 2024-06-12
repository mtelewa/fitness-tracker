from . import views
from django.urls import path


urlpatterns = [
    path('nutrition/', views.index, name='nutrition'),
]