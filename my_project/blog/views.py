from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author': 'ReaganBarrington',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'September 26, 2020',
#     },
#         {
#         'author': 'TeddyDickerson',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'September 28, 2020',
#     },
# ]

# Instead of dummy data, let's import run a query from our post model 



# views
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})