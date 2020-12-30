from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import CropOrder
from django.forms import ModelForm


class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(ModelForm):
    class Meta:
        model = CropOrder
        fields = ['name', 'cost', 'qty', 'location']
