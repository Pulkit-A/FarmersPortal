from django.shortcuts import render, redirect
from django.http import HttpResponse
from crops.models import Crop
from .forms import UserAddForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    Crops = Crop.objects.all()
    return render(request, 'index.html', {'Crops': Crops})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserAddForm()
        if request.method == 'POST':
            form = UserAddForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username= username, password = password)
            login(request, username)
            return redirect('home')
    
    return render(request, 'login.html')


def logout(request):
        logout(request)
        return redirect('login')


def policy_view(request):
    return render(request, 'policies.html')


def learn_view(request):
    return render(request, 'learning.html')


def about_view(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def cart_view(request):
    return render(request, 'cart.html')