from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='home'),
    path('new/', views.PostCreate.as_view(), name='developer'),
    path('posts/', views.PostIndexTwo.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('about/', views.about, name='about'),
    path('accounts/register/', views.register, name='register')
]