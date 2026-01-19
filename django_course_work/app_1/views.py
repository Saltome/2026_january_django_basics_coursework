from django.shortcuts import render
from .models import Time
from django.http import JsonResponse


def view_time(request):
    time, created = Time.objects.get_or_create(pk=1)
    return render(request, 'resources.html', {'time': time.value, "progress": 100 * (time.value%1)})


def update_resource(request):
    time, created = Time.objects.get_or_create(pk=1)
    time.value += 0.1
    time.save()
    return JsonResponse({
        "time": time.value,
        "progress": 100 * (time.value%1)
    })