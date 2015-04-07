# Create your views here.
from django.shortcuts import render


def HomeView(request):
    return render(request, 'index.html')
