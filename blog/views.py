from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})
from django.shortcuts import render, get_object_or_404 # new

# Create your views here.
# blog/views.py
from .models import Post
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'home.html', {'posts': posts})
def post_detail(request, pk): # new
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_detail.html", {"post": post})
