from . import views
from django.urls import path

urlpatterns = [
    path('', views.list, name="list"),
    path("<int:post_id>/", views.detail, name="detail")
]
