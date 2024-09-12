from django.contrib import admin  
from .models import Post,Category,Tag

# Register your models here.  
class PostAdmin(admin.ModelAdmin):  
    # list_filter = ["created_time"] 
   list_display = ["title","active","id"]
   date_hierarchy=("created_time")


class CategoryAdmin(admin.ModelAdmin):  
 # list_filter = ["created_time"] 
    list_display = ["title","active"]



class TagAdmin (admin.ModelAdmin):
    list_display=["title","active"]



admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)