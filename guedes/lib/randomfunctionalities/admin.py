from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Network, Microformat


class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['icon', 'order']


admin.site.register(Network, NetworkAdmin)
admin.site.register(Microformat, SingletonModelAdmin)
