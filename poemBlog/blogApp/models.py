from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):

    options = {
        ("draft", "Draft"),
        ("published", "Published")
    }

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")
    upload_image = models.ImageField(upload_to ='uploads/', null=True, blank=True)

    class Meta():
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

