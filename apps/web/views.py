from django.shortcuts import render

def index(request):
    return render (request, "templates/index.html")
# Create your views here.
