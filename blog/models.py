from django.db import models
from django.urls import reverse

class Author(models.Model):
    author_name = models.CharField(max_length=255)
    author_about = models.TextField()
    author_image = models.FileField(null=True, blank=True)
    author_date_created = models.DateTimeField(auto_now_add=True)
    author_date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.author_name

class Post(models.Model):
    title = models.CharField(max_length=255, default="title")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default="Autor")
    slug = models.CharField(max_length=255, unique=True)
    post = models.TextField(default='')
    post_date_created = models.DateTimeField(auto_now_add=True)
    post_date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    
    

