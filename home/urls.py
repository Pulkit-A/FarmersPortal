from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('learn/', views.learn_view),
    path('policies/', views.policy_view),
    path('about/', views.about_view),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view),
    path('cart/', views.cart_view)
]