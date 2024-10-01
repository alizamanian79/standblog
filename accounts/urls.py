from django.urls import path  
from .views import login_view  

app_name = 'accounts'  

urlpatterns = [  
    path('login/', login_view, {'mode': 'sign-in'}, name='login'),
    path('login/<str:mode>/', login_view, name='mode'), 
]