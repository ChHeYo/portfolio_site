from django.contrib import admin

from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )
    list_display_links = ('title', )

admin.site.register(Post, PostAdmin)