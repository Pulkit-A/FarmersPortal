from . import views
from django.urls import path


urlpatterns = [
    path('crops/', views.crops_view),
    path('crops/description/<str:pk>/', views.crop_view),
]