from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def status(request):
    return HttpResponse(
        "World Building app is running.",
        content_type="text/plain"
    )

from django.shortcuts import render, get_object_or_404, redirect
from .models import World
from .forms import WorldForm

def world_list(request):
    worlds = World.objects.all()
    return render(request, 'world_building/world_list.html', {'worlds': worlds})

def world_create(request):
    if request.method == 'POST':
        form = WorldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('world-list')
    else:
        form = WorldForm()
    return render(request, 'world_building/world_form.html', {'form': form})

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

