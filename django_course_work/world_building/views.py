from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from generators.name_generators.world_names import generate_world_name

def status(request):
    return JsonResponse({"status": "ok"})

from django.shortcuts import render, get_object_or_404, redirect
from .models import World
from .forms import WorldForm

def world_list(request):
    worlds = World.objects.all()
    return render(request, 'world_building/world_list.html', {'worlds': worlds})

def world_create(request):
    if request.method == 'POST':
        world = WorldForm(request.POST)
        if world.is_valid():
            world.save()
            return redirect('world-list')
    else:
        world = WorldForm(initial={
            "name": generate_world_name()
        })
    return render(request, 'world_building/world_form.html', {'form': world})
def generate_world_name_view(request):
    seed = request.GET.get("seed")

    try:
        seed = float(seed) if seed is not None else None
    except ValueError:
        seed = None

    return JsonResponse({
        "name": generate_world_name(seed)
    })
def world_detail(request, pk):
    world = get_object_or_404(World, pk=pk)
    return render(request, 'world_building/world_detail.html', {'world': world})

def world_update(request, pk):
    world = get_object_or_404(World, pk=pk)
    if request.method == 'POST':
        form = WorldForm(request.POST, instance=world)
        if form.is_valid():
            form.save()
            return redirect('world-detail', pk=world.pk)
    else:
        form = WorldForm(instance=world)
    return render(request, 'world_building/world_form.html', {'form': form})

def world_delete(request, pk):
    world = get_object_or_404(World, pk=pk)
    if request.method == 'POST':
        world.delete()
        return redirect('world-list')
    return render(request, 'world_building/world_confirm_delete.html', {'world': world})

