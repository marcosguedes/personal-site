from django.conf.urls import patterns, url

from django.contrib import admin
from .views import HomePageView

admin.autodiscover()

urlpatterns = patterns('',
                        url(r'^$', HomePageView.as_view(), name='home'),
                        )