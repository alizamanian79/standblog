from django.db import models

# Create your models here.
class Post (models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    Active=models.BooleanField(default=False)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Post"
        verbose_name_plural = "Post's"