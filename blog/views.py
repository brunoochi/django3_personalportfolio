from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {"blogs": blogs})

def detail(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'blog/detail.html', {"id": post})