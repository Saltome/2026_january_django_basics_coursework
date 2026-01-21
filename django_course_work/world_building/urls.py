from django.urls import path
from . import views

from django.urls import path
from .views import status

urlpatterns = [
    path('', status, name='world-building-status'),

]
