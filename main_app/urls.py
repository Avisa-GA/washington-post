from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view()),
    path('new/', views.PostCreate.as_view()),
    path('posts/', views.PostIndexTwo.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view()),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view()),
    path('about/', views.about),
    path('accounts/register/', views.register)
]