from django.shortcuts import render
from .models import Time
from django.http import HttpResponse


def view_time(request):
    time, created = Time.objects.get_or_create(pk=1)
    return render(request, 'resources.html', {'time': time})


def update_resource(request):
    time, created = Time.objects.get_or_create(pk=1)
    time.value += 1
    time.save()
    return HttpResponse(str(time.value))