from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages


# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{"posts":posts})

def post(req,id):
    
    current_post = Post.objects.get(id=id)
    if current_post is not None:
        return render(req,'post.html',{"posts":current_post})
        pass
        
    else:
        messages.info(req, "Post not found") 