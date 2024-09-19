from django.urls import path
from .views import Index,about,contact

app_name='website'
urlpatterns = [
    path("",Index,name="index"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
]
