from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def status(request):
    return HttpResponse(
        "World Building app is running.",
        content_type="text/plain"
    )
