from django.shortcuts import render

# Create your views here.
def login_view(request):

    context={"form"}
    return render(request,'accounts/login.html', context)