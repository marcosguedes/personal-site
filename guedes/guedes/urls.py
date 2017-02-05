from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import debug_toolbar

from django.contrib import admin
from personalsite.views import HomePageView
admin.autodiscover()

urlpatterns = patterns('',
                            url(r'^admin/', include(admin.site.urls)),
                            url(r'^robots.txt$', include('robots.urls')),
                            # url(r'^humans\.txt$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
                            url(r'^blog/', include('blog.urls', namespace='blog')),
                            (r'^ckeditor/', include('ckeditor_uploader.urls')),
                            url(r'^interest/', include('aboutme.urls')),
                            url(r'^', include('personalsite.urls')),
                            )

# debug static and media fiels urls
if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           url(r'', include('django.contrib.staticfiles.urls')),
                           (r'^404/', TemplateView.as_view(template_name="404.html")),
                           (r'^500/', TemplateView.as_view(template_name="500.html")),
                           (r'^503/', TemplateView.as_view(template_name="503.html")),
                           url(r'^__debug__/', include(debug_toolbar.urls)),
                           ) + urlpatterns

urlpatterns += staticfiles_urlpatterns()
