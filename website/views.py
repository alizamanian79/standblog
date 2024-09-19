from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
# Create your views here.

def Index(request):
    return render(request,"website/index.html")

def about(request):
    return render(request,"website/about.html")

def contact(request):

    if request.method=="POST":
        forms=ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
        
    forms=ContactForm()  
    return render(request,"website/contact.html",{"forms":forms})