from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . models import Post
from django.template import loader
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.all()
    pages = Paginator(posts,3)
    page_number = request.GET.get('page')
    page_obj = pages.get_page(page_number)
    context = {
        'posts':page_obj
    }
    return render(request,'blogdev/post.html',context)
   
    

def post(request,id):
   post = get_object_or_404(Post,pk=id)
   return render(request,'blogdev/detail.html',{'post':post})