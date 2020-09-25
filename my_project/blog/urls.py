from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    # links to views file
]
