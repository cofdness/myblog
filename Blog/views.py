from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .form import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'Blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})