from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Network, Microformat
from modeltranslation.admin import TranslationAdmin


class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['icon', 'order']


class MicroformatAdmin(TranslationAdmin, SingletonModelAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Network, NetworkAdmin)
admin.site.register(Microformat, MicroformatAdmin)
