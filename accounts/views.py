from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def login_view(request, mode):  
    if mode == "sign-in":  
        if request.method == "POST":  
            username = request.POST.get("username")  
            password = request.POST.get("password")  
            result = authenticate(request, username=username, password=password)  
            if result is not None:  
                login(request, result)
                messages.success(request, "You are logged in successfully")  
                return redirect("/")   
            else:  
                messages.error(request, "Wrong username or password")  

    context = {"form": AuthenticationForm()} 
    return render(request, 'accounts/login.html', context)  