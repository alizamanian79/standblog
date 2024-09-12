from django.urls import path
from .views import Index,About,Contact

app_name='website'
urlpatterns = [
    path("",Index,name="index"),
    path("about/",About,name="about"),
    path("contact/",Contact,name="contact"),
]
