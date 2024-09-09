from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post (models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    Active=models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="blog/images/",default="blog/images/default.jpg")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Post"
        verbose_name_plural = "Post's"