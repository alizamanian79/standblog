from django.contrib import admin  
from .models import Post,Category,Comment

# Register your models here. 

class CommentInline(admin.StackedInline):
    model = Comment
    fields = ["name", "email","subject","message","active"]
    extra = 0


@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):  
    # list_filter = ["created_time"] 
   list_display = ["title","active","id"]
   date_hierarchy=("created_time")
   inlines = [CommentInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  
    list_display = ["title",]

