from django.urls import path
from . import views

urlpatterns = [
    path('give-rating/', views.give_rating, name='give_rating'),
]