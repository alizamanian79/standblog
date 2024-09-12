from django.shortcuts import render, get_object_or_404  
from .models import Post,Tag,Category

# Create your views here.  
def blog(request,**kwargs):  
    posts = Post.objects.filter(active=True)  
    tags = Tag.objects.filter(active=True)
    categories=Category.objects.filter(active=True)

    if kwargs.get("cat"):
        posts = Post.objects.filter(category__title=kwargs["cat"])  

    if kwargs.get("tag"):
        posts = Post.objects.filter(tag__title=kwargs["tag"])  

    if kwargs.get("auth"):  
        posts = posts.filter(author__username=kwargs["auth"])

    if kwargs.get("nat"):  
        posts = Post.objects.filter(nationality__title=kwargs["nat"])

    context = {"posts": posts,"tags":tags,"categories":categories}  
    return render(request, "blog/blog.html", context)  

def post_details(request, num): 
    post = get_object_or_404(Post, id=num, active=True)  
    context = {"post": post} 
    return render(request, "blog/post-details.html", context)