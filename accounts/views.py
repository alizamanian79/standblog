from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):  
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            messages.success(request,"you login successfully")
            return redirect('/')
        
        elif not user:
            messages.error(request,"your username and password are incorrect")

    context ={"form":AuthenticationForm} 
    return render(request, 'accounts/login.html', context)  


@login_required
def logout_view(request):
    messages.success(request,"you logout successfully")
    return redirect('/')

def checking_view(request):
    if request.user.is_authenticated:
        messages.success(request, "I know you")
    else:
        messages.success(request, "stranger")
    
    return("/")