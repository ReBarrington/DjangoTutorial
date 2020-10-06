from django.urls import path
from . import views

# endpoints

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    # links to views file
]
