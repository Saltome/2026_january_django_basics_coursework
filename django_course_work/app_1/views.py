from django.shortcuts import render
from .models import Time, Land
from django.http import JsonResponse


def view_resources(request):
    time, created = Time.objects.get_or_create(pk=1)
    land, created = Land.objects.get_or_create(pk=1)
    return render(request, 'resources.html', {'time': time.value, "progress": 100 * (time.value%1), "land": land.value})

def update_resource(request):
    time, created = Time.objects.get_or_create(pk=1)
    time.value += 0.1
    time.save()
    land, created = Land.objects.get_or_create(pk=1)
    land.value += 1
    land.save()
    return JsonResponse({
        "time": time.value,
        "land": land.value,
        "progress": 100 * (time.value%1)
    })