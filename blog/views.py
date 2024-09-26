from django.shortcuts import render, get_object_or_404  
from .models import Post  , Comment
from django.db.models import Q  
from .forms import CommentForm  
from django.shortcuts import redirect
from django.contrib import messages  
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
    comment=Comment.objects.filter(post=post, active=True)

    if request.method=="POST":
        forms=CommentForm(request.POST)
        if forms.is_valid():
            forms.instance.post=post
            forms.save()
            messages.success(request, "Comment has been posted successfully")
            return redirect('/')


    forms=CommentForm()
    context = {"post": post,"comment":comment,"form":forms}     
    return render(request, "blog/post-details.html", context)