from django.conf.urls import patterns, url

from django.contrib import admin
from .views import InterestDetailView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^(?P<slug>(.*))/$', InterestDetailView.as_view(), name='interest_detail'),
                       )
