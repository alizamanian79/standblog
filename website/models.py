from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=250)
    message=models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"