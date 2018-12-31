from django.conf.urls import url

from django.contrib import admin
from .views import HomePageView, AboutPageView

admin.autodiscover()

urlpatterns = [
    url(r'^about/$', AboutPageView.as_view(), name='about'),
    url(r'^$', HomePageView.as_view(), name='home'),
]