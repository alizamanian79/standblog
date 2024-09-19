from django.shortcuts import render, get_object_or_404  
from .models import Post  
from django.db.models import Q  

# Create your views here.  
def blog(request, **kwargs):  
    posts = Post.objects.filter(active=True)  

    if kwargs.get("cat"):  
        posts = posts.filter(category__title=kwargs["cat"])  

    if kwargs.get("auth"):  
        posts = posts.filter(author__username=kwargs["auth"])  

    if kwargs.get("tag"):  
        posts = posts.filter(tags__name=kwargs["tag"])  

    if search := request.GET.get("q"):
        posts=posts.filter(Q(title__icontains=search) | Q(description__icontains=search))


    context = {"posts": posts}  
    return render(request, "blog/blog.html", context)  



def post_details(request, num):   
    post = get_object_or_404(Post, id=num, active=True)  
    context = {"post": post}   
    return render(request, "blog/post-details.html", context)