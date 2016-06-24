from django.contrib import admin

# Register your models here.
from blog.models import *

class PostModelAdmin (admin.ModelAdmin):
    list_display = ['title', 'updated', 'created']
    list_display_links = ['title']
    list_filter = ['updated', 'created', 'categories']
    search_fields = ['title', 'content', 'categories']
    prepopulated_fields = {
        'slug': ('title',),
    }

    class Meta:
        model = Post


class CategoryModelAdmin (admin.ModelAdmin):
    class Meta:
        model = Post
        
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
