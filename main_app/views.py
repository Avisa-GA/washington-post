from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')