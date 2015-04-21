from django.contrib import admin
from django.utils.translation import ugettext as _
from .models import CookieDisclaimer
from solo.admin import SingletonModelAdmin
from modeltranslation.admin import TranslationAdmin


class CookieDisclaimerAdmin(TranslationAdmin, SingletonModelAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(CookieDisclaimer, CookieDisclaimerAdmin)
