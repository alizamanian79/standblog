from django.shortcuts import render, redirect  
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
from django.contrib.auth import login, logout, authenticate  
from django.contrib import messages  
from django.contrib.auth.decorators import login_required  

# Create your views here.  
def login_view(request):  
    if request.method == 'POST':  
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():  
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')  
            user = authenticate(request, username=username, password=password)  
            if user is not None:  
                login(request, user)  
                messages.success(request, "You logged in successfully.")  
                return redirect('/') 
            else:  
                messages.error(request, "Your username and password are incorrect.")  
        else:  
            messages.error(request, "Invalid form submission.")  
    else:  
        form = AuthenticationForm()  
    
    context = {"form": form}   
    return render(request, 'accounts/login.html', context)  

@login_required  
def logout_view(request):  
    logout(request)  
    messages.success(request, "You logged out successfully.")  
    return redirect('/')  # Redirect to the desired page after logout  

def signup_view(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  
            login(request, user)  # Automatically log in after signup  
            messages.success(request, "You signed up successfully.")  
            return redirect('/')  # Redirect to the desired page after signup  
        else:  
            messages.error(request, "Please correct the error below.")  
    else:  
        form = UserCreationForm()  

    context = {"form": form}   
    return render(request, 'accounts/signup.html', context)  # Make sure to point to your signup template