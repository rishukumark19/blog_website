from django.contrib import admin

# Register your models here.
from .models import Post
class PostAdmin(admin.ModelAdmin): # new
    list_display = (
        "title",
        "author",
        "body",
        )
admin.site.register(Post, PostAdmin) # new
