from django.urls import path
from .views import Blog,Post


app_name='blog'
urlpatterns = [
    path("",Blog ,name='blog'),
    path("post-details/",Post ,name='post-details')
]
