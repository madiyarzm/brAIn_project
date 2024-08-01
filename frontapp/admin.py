
# importing admin and posts model 
from django.contrib import admin 
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin 
  
# creating admin class 
class blogadmin(SummernoteModelAdmin): 
    # displaying posts with title slug and created time 
    list_display = ('title', 'slug', 'status', 'created_on') 
    list_filter = ("status", ) 
    search_fields = ['title', 'content'] 
    # prepopulating slug from title 
    prepopulated_fields = {'slug': ('title', )} 
    summernote_fields = ('content', ) 
  
# registering admin class 
admin.site.register(Post, blogadmin,)
admin.site.register(Category)