from django.contrib import admin
from .models import Tag, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'published']
    list_editable = ['date_created', 'published']
    list_filter = ['tags']
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal= ['tags']


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
