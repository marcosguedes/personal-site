from django.contrib import admin
from .models import Category, Interest

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'active']
    list_editable = ['order', 'active']
    prepopulated_fields = {"slug": ("title",)}


class InterestAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'active']
    list_editable = ['order', 'category', 'active']
    list_filter = ['category', 'active']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Interest, InterestAdmin)
