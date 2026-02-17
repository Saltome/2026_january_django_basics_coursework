from django.shortcuts import render

def tilemap_view(request):
    return render(request, "tilemap/tilemap.html")
