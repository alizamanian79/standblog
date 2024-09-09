from django.shortcuts import render, get_object_or_404  
from .models import Post

# Create your views here.  
def blog(request,**kwargs):  
    posts = Post.objects.filter(Active=True)  

    if kwargs.get("cat"):
        posts = Post.objects.filter(category__title=kwargs["cat"])  

    if kwargs.get("auth"):  
        posts = posts.filter(author__username=kwargs["auth"])


    context = {"posts": posts}  
    return render(request, "blog/blog.html", context)  

def post_details(request, num): 
     
    post = get_object_or_404(Post, id=num, Active=True)  
    context = {"post": post} 
    return render(request, "blog/post-details.html", context)