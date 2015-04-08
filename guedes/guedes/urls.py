from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from solid_i18n.urls import solid_i18n_patterns
from guedes.sitemap import sitemaps
from randomfunctionalities.views import HomeView
admin.autodiscover()

urlpatterns = solid_i18n_patterns('',
                            url(r'^admin/', include(admin.site.urls)),

                            url(r'^robots.txt$', include('robots.urls')),
                            # url(r'^humans\.txt$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
                            url(r'^blog/', include('zinnia.urls')),
                            url(r'^comments/', include('django.contrib.comments.urls')),
                            (r'^ckeditor/', include('ckeditor.urls')),
                            url(r'^sitemap.xml$', 'index', {'sitemaps': sitemaps}),
                            url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
                            url(r'^$', HomeView, name='home'),
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
                           ) + urlpatterns

urlpatterns += staticfiles_urlpatterns()
