
from operator import mod
from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, DetailView
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

class PostIndexTwo(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

def about(request):
    abouts = About.objects.all()
    return render(request, 'about.html', {'abouts': abouts})


class PostDelete(DeleteView):
    model = Post
    template_name = 'confirm_delete.html'
    success_url = '/'

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post.html'
    success_url = '/'


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post.html'
    success_url = "/"