from django.db import models
from django.shortcuts import render
from .models import Post

def list(request):
    post_list = Post.objects.all()
    context = {"post_list": post_list}
    return render(request, 'blog/list.html', context)
