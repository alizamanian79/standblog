from django.contrib import admin  
from .models import Post,Category

# Register your models here.  
class PostAdmin(admin.ModelAdmin):  
    # list_filter = ["created_time"] 
   list_display = ["title","Active","id"]
   date_hierarchy=("created_time")


class CategoryAdmin(admin.ModelAdmin):  
 # list_filter = ["created_time"] 
    list_display = ["title"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)