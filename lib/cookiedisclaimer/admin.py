from django.contrib import admin
from django.utils.translation import ugettext as _
from .models import CookieDisclaimer
from solo.admin import SingletonModelAdmin


admin.site.register(CookieDisclaimer, SingletonModelAdmin)
