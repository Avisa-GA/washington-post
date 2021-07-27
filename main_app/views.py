
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .models import About

# Create your views here.
# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})

# Index page as a Class-based View
class PostIndex(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

def about(request):
    abouts = About.objects.all()
    return render(request, 'about.html', {'abouts': abouts})

def post(request):
    return render(request, 'post.html')

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post.html'
    success_url = '/posts/'