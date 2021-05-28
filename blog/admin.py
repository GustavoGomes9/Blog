from django.db import models
from .models import Author, Post
from django.contrib import admin

@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "post", "slug", "post_date_created", "post_date_updated")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("author_name", "author_about", "author_image", "author_date_created", "author_date_updated")
