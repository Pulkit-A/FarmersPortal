from django.shortcuts import render
from django.http import HttpResponse
from crops.models import Crop


def index(request):
    Crops = Crop.objects.all()
    return render(request, 'index.html', {'Crops': Crops})