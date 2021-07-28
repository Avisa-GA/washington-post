
from operator import mod

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post
from .models import About

# Create your views here.
# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})

# Index page as a Class-based View
def register(request):
    errors = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            errors = form.errors
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form, 'errors': errors})

class PostIndex(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class PostIndexTwo(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

def about(request):
    abouts = About.objects.all()
    return render(request, 'about.html', {'abouts': abouts})


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'confirm_delete.html'
    success_url = '/'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post.html'
    success_url = "/"