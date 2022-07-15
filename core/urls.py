from django.urls import path
from .views import subscription

urlpatterns = [ 
    path('subscription/', subscription)
]