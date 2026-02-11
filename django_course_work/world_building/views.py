from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from generators.name_generators.world_names import generate_world_name
from generators.political_generators.political_entity import generate_political_entities


from django.shortcuts import render, get_object_or_404, redirect

from .models import World
from .models import PoliticalEntity

from .forms import WorldForm
from .forms import PoliticalEntityForm

def status(request):
    return JsonResponse({"status": "ok"})

def world_list(request):
    worlds = World.objects.all()
    return render(request, 'world_building/world_list.html', {'worlds': worlds})

def world_create(request):
    if request.method == 'POST':
        world_form = WorldForm(request.POST)
        if world_form.is_valid():
            world_form.save()
            seed = request.GET.get("seed")
            generate_political_entities(world_form.instance)
            return redirect('world-list')
    else:
        world_form = WorldForm(initial={
            "name": generate_world_name()
        })
    return render(request, 'world_building/world_form.html', {'form': world_form})
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


def political_entity_detail(request, pk):
    entity = get_object_or_404(PoliticalEntity, pk=pk)
    return render(
        request,
        "world_building/political_entity_detail.html",
        {"entity": entity}
    )

def political_entity_create(request, world_pk):
    world = get_object_or_404(World, pk=world_pk)

    if request.method == "POST":
        form = PoliticalEntityForm(request.POST)
        if form.is_valid():
            entity = form.save(commit=False)
            entity.world = world
            entity.save()
            return redirect("world-detail", pk=world.pk)
    else:
        form = PoliticalEntityForm()

    return render(
        request,
        "world_building/political_entity_form.html",
        {"form": form, "world": world}
    )

def political_entity_update(request, pk):
    entity = get_object_or_404(PoliticalEntity, pk=pk)

    if request.method == "POST":
        form = PoliticalEntityForm(request.POST, instance=entity)
        if form.is_valid():
            form.save()
            return redirect("political-entity-detail", pk=entity.pk)
    else:
        form = PoliticalEntityForm(instance=entity)

    return render(
        request,
        "world_building/political_entity_form.html",
        {"form": form, "entity": entity, "world": entity.world}
    )

def political_entity_delete(request, pk):
    entity = get_object_or_404(PoliticalEntity, pk=pk)
    world = entity.world

    if request.method == "POST":
        entity.delete()
        return redirect("world-detail", pk=world.pk)

    return render(
        request,
        "world_building/political_entity_confirm_delete.html",
        {"entity": entity, "world": world}
    )
