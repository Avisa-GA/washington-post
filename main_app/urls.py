from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view()),
    path('new/', views.PostCreate.as_view()),
    path('about/', views.about),
]