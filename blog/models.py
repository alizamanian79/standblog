from django.db import models  
from django.contrib.auth.models import User  


# Create your models here.  
class Post(models.Model):  
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    active = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)  
    updated_time = models.DateTimeField(auto_now=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    image = models.ImageField(upload_to="blog/images/", default="blog/images/default.jpg")  
    category = models.ManyToManyField("category",null=True, blank=True)
    tag = models.ManyToManyField("tag", blank=True,null=True)

    def __str__(self):  
        return self.title  

    class Meta:  
        verbose_name = "Post"  
        verbose_name_plural = "Posts"


class Category(models.Model):  
    title = models.CharField(max_length=150)
    active=models.BooleanField(null=True,default=True)
    created_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)  
    updated_time = models.DateTimeField(auto_now=True,blank=True,null=True) 
    def __str__(self):  
        return self.title
    
class Tag(models.Model):  
    title = models.CharField(max_length=150)  
    active=models.BooleanField(null=True,default=True)
    created_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)  
    updated_time = models.DateTimeField(auto_now=True,blank=True,null=True) 

    def __str__(self):  
        return self.title