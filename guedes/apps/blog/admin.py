from django.contrib import admin
from .models import Tag, Post, Content


class ContentInlineAdmin(admin.TabularInline):
    model = Content
    extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [ContentInlineAdmin]
    list_display = ['title', 'date_created', 'published']
    list_editable = ['date_created', 'published']
    list_filter = ['tags']
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal= ['tags']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, admin.ModelAdmin)
