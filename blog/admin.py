from django.contrib import admin

# Register your models here.
from blog.models import *


class PostModelAdmin(admin.ModelAdmin):

    class Meta:
        model = Post

    list_display = ['title', 'updated', 'created']
    list_display_links = ['title']
    list_filter = ['updated', 'created', 'categories']
    search_fields = ['title', 'content']
    prepopulated_fields = {
        'slug': ('title',),
    }


class CategoryModelAdmin(admin.ModelAdmin):

    class Meta:
        model = Post

    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class ReviewModelAdmin(admin.ModelAdmin):

    class Meta:
        model = Review
    list_display = ['post', 'user', 'star', 'comment']
    list_display_links = ['comment']
    list_filter = ['post', 'user', 'star']
    search_fields = ['comment', 'post', 'user']


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Review, ReviewModelAdmin)
