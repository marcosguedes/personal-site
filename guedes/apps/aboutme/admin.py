from django.contrib import admin
from .models import Category, Interest
from modeltranslation.admin import TranslationAdmin


class BaseAdmin(TranslationAdmin):
    list_display = ['title', 'order', 'active']
    list_editable = ['order', 'active']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class CategoryAdmin(BaseAdmin):
    prepopulated_fields = {"slug": ("title",)}


class InterestAdmin(BaseAdmin):
    list_display = ['title', 'category', 'order', 'active']
    list_editable = ['order', 'category', 'active']
    list_filter = ['category', 'active']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Interest, InterestAdmin)
