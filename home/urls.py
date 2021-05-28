from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('Home', views.Home, name='Home'),
    path('Contact', views.Contact, name='Contact'),

]
