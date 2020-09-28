from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'ReaganBarrington',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 26, 2020',
    },
        {
        'author': 'TeddyDickerson',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 28, 2020',
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})