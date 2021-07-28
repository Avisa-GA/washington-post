from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.content




class About(models.Model):
    title_about = models.CharField(max_length=300)
    content_about = models.CharField(max_length=1000)

    def __str__(self):
            return self.title_about


    def __str__(self):
        return self.content_about