from django.urls import path
from . import views

from django.urls import path
from .views import status

world_urlpatterns = [
    path('', views.world_list, name='world-list'),
    path('create/', views.world_create, name='world-create'),
    path('<int:pk>/', views.world_detail, name='world-detail'),
    path('<int:pk>/edit/', views.world_update, name='world-update'),
    path('<int:pk>/delete/', views.world_delete, name='world-delete'),
    path("generate-name/", views.generate_world_name_view,name="generate-world-name"
),

]

urlpatterns = [
    path('status/', status, name='world-building-status'),
] + world_urlpatterns
