from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
from django.template import loader


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'blogdev/post.html',context)
   
    