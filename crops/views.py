from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Crop
import random


@login_required(login_url='login')
def crops_view(request):
    crops = list(Crop.objects.all())
    rcrops = random.sample(crops,9)
    context = {'rcrops':rcrops}
    return render(request, 'crops.html', context)


@login_required(login_url='login')
def crop_view(request, pk):
    crop = Crop.objects.get(id=pk)
    context = {'crop':crop}
    return render(request, 'crop.html', context)