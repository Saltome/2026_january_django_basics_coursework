from django.urls import path
from . import views

from django.urls import path
from .views import status

generators_urlpatterns = [
    path('', status, name='generators_hub'),
]

urlpatterns = [
    path('status/', status, name='generators-status'),
] + generators_urlpatterns
