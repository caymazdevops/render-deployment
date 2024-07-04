from django.shortcuts import render, get_object_or_404
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

def index(request):
    posts = Post.objects.all()
    return render(request, 'books/blog.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'books/post_detail.html', {'post': post})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer