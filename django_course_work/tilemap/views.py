from django.shortcuts import render, get_object_or_404
from world_building.models import World
from .generation.terrain import generate_tilemap

def tilemap_view(request):
    return render(request, "tilemap/tilemap.html")



def world_tilemap(request, world_pk):
    world = get_object_or_404(World, pk=world_pk)

    width = 50
    height = 50
    tiles = generate_tilemap(width, height, world.seed)

    return render(
        request,
        "tilemap/tilemap.html",
        {
            "world": world,
            "tiles": tiles,
            "width": width,
            "height": height,
        }
    )
