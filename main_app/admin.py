from django.contrib import admin
from .models import About, Post
# Register your models here.
admin.site.register(Post)
admin.site.register(About)
class PostAdminArea(admin.AdminSite):
    site_header = "The Washington Post Admin Area"
    login_template = 'post/admin/login.html'

post_site = PostAdminArea(name='PostAdmin')
post_site.register(Post)
post_site.register(About)