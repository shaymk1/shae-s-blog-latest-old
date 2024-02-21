from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Post, Tags


def home(request):
    model = Post
    posts = Post.objects.all().order_by("created_at")
    tags = Tags.objects.all()
    context = {
        "model": model,
        "posts": posts,
        "tags": tags

    }
    return render(request, "blog/index.html", context)


def detailed_post(request, slug):
    model = Post
    post = get_object_or_404(Post, slug=slug)
    context = {
      "model": model,
      "post": post,  
    }
    return render(request, "blog/post.html", context)


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")
