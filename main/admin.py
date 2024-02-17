from django.contrib import admin
from .models import Post, Comment, Bookmark


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    
admin.site.register(Comment)
admin.site.register(Bookmark)

    
    