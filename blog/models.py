# from unicodedata import category
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    image = models.ImageField(
        null=True, blank=True, 
        upload_to="articles",
        default="placeholder.png"
        )
    category = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    time_required_to_read = models.CharField(
        max_length=250, 
        default="2 Min Read"
        )
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, null=True)  # max_length=250,unique=True 
    intro = models.TextField(blank=True)
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    author_image = models.ImageField(
         null=True, blank=True, 
         upload_to="articles",
         default="placeholder.png")

    class Meta:
        ordering = ("-created_at",)  # decending order

    def __str__(self):
        return self.title
    

class Tags(models.Model):
    tag = models.CharField(max_length=250)
    
    def __str__(self):
        return self.tag
