from django.contrib import admin  
from .models import Post  

# Register your models here.  
class PostAdmin(admin.ModelAdmin):  
    # list_filter = ["created_time"] 
   list_display = ["title","Active","id"]
   date_hierarchy=("created_time")

admin.site.register(Post, PostAdmin)