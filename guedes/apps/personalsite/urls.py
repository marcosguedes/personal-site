from django.conf.urls import url

from django.contrib import admin
from .views import HomePageView

admin.autodiscover()

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]