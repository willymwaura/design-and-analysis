from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('push/', views.push, name='push'),
    path('pop/', views.pop, name='pop'),
    path('top/', views.top, name='top'),
    path('length/', views.length, name='length'),
    path('is_empty/', views.is_empty, name='is_empty'),
]
