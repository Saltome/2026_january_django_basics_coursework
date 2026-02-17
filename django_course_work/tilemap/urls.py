from django.urls import path
from . import views

urlpatterns = [
    path("", views.tilemap_view, name="tilemap-home"),
]
