from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('blogPost/<str:title>/<int:id>', views.blogPost, name="blogPost"),
]
