from django.urls import path
from . import views

urlpatterns = [
    path('referrals/', views.referral_list, name='referral_list'),
]
