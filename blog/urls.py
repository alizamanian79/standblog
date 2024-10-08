from django.urls import path
from .views import blog,post_details

app_name='blog'
urlpatterns = [
    path("",blog ,name='blog'),
    path("<int:num>/",post_details ,name='post-detail'),
    path("category/<cat>/",blog ,name='category'),
    path("tag/<tag>/",blog ,name='tag'),
    path("author/<str:auth>/",blog ,name='author'),
]
