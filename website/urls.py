from django.urls import path
from . import views
app_name="website"

urlpatterns = [
    path('',views.index,name="index"),
    path('about-us/',views.about_us,name="about-us"),
    path('contact/',views.contact,name="contact"),
    path('post-details/',views.post_details,name="post-details"),
    path('blog/',views.blog,name="blog"),
    
]
