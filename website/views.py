from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,"website/index.html")

def About(request):
    return render(request,"website/about.html")

def Contact(request):
    return render(request,"website/index.html")