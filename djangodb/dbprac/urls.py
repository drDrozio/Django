from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('join',views.join, name='join'),
]
