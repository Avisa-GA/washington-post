from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostIndex.as_view()),
    path('posts/new/', views.PostCreate.as_view()),
    path('about/', views.about),
]