from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.list, name="list"),
    path("<slug:slug>/", views.detail, name="detail")
]
