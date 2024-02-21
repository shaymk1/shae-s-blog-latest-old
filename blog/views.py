from django.shortcuts import render
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


def about(request):
    return render(request, "blog/about.html")


def post(request):
    return render(request, "blog/post.html")


def contact(request):
    return render(request, "blog/contact.html")
