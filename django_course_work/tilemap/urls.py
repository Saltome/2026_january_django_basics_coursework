from django.urls import path
from . import views

urlpatterns = [
    # path("", views.tilemap_view, name="tilemap-home"),
    path(
        "world/<int:world_pk>/",
        views.world_tilemap,
        name="world-tilemap"
    ),

]
