from django.db import models  
from accounts.models import CustomUser
from taggit.managers import TaggableManager

# Create your models here. 
# 
# 


class Category(models.Model):  
    title = models.CharField(max_length=150)
    def __str__(self):  
        return self.title
 

class Post(models.Model):  
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    active = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)  
    updated_time = models.DateTimeField(auto_now=True)  
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)  
    image = models.ImageField(upload_to="blog/images/", default="blog/images/default.jpg")  
    category = models.ManyToManyField(Category)
    tags = TaggableManager()

    def __str__(self):  
        return self.title  

    class Meta:  
        verbose_name = "Post"  
        verbose_name_plural = "Posts"



class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=250)
    message=models.TextField()
    active = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)  
    updated_time = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_time']