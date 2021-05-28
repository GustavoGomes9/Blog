from django.db import models
from django.http.response import Http404
from django.shortcuts import render
from .models import Post

def list(request):
    post_list = Post.objects.all()
    context = {"post_list": post_list}
    return render(request, 'blog/list.html', context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk= post_id)
    except Post.DoesNotExist:
        raise Http404("Valor não encontrado.")
    return render(request, 'blog/detail.html', {"post": post})

# https://cryptohayes.medium.com/farb-l-ast-off-go-de6f5bb7a099 template