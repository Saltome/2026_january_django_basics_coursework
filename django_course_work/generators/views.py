from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def status(request):
    return JsonResponse({"status": "ok"})