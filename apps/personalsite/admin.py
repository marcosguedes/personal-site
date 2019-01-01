from django.contrib import admin
from .models import HomePage, AboutPage
from solo.admin import SingletonModelAdmin


admin.site.register(HomePage, SingletonModelAdmin)
admin.site.register(AboutPage, SingletonModelAdmin)
