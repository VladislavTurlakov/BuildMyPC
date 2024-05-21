from django.urls import path
from .views import os, ssd, cpucooler, case, cpu, gpu, motherboard, ram, powersupply
from . import views

urlpatterns = [
    path('os/', os, name='os'),
    path('ssd/', ssd, name='ssd'),
    path('cpucooler/', cpucooler, name='cpucooler'),
    path('case/', case, name='case'),
    path('cpu/', cpu, name='cpu'),
    path('gpu/', gpu, name='gpu'),
    path('motherboard/', motherboard, name='motherboard'),
    path('ram/', ram, name='ram'),
    path('powersupply/', powersupply, name='powersupply'),
    path('', views.hello_world, name='hello_world'),
]