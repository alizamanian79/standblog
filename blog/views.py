from django.shortcuts import render

# Create your views here.
def Blog(request):
    return render(request , "blog/blog.html")

def Post(request):
    return render(request , "blog/post-details.html")