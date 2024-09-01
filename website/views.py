from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    return render(request,"website/index.html")

def about_us(request):
    return render(request,"website/about.html")


def contact(request):
    return render(request,"website/contact.html")


def post_details(request):
    return render(request,"website/post-details.html")


def blog(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,"website/blog.html",context)