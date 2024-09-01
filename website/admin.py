from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin (admin.ModelAdmin):
    data_hierarchy="created_time"
    list_display=['id','title','description','author','created_time','updated_time']
    search_fields=('title','description')
    list_filter=['active']


admin.site.register(Post,PostAdmin)