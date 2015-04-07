from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Ucomment this line for favicon url
    url(r'^robots.txt$', include('robots.urls')),
    url(r'^humans\.txt$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='%ssite/images/favicon.ico' % settings.STATIC_URL)),

    # url(r'^admin_tools/', include('admin_tools.urls')),  # before admin/
    # url(r'^maintenance/', include('controlpanel.urls')),
)

# add cms urls if is installed
if 'cms' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^', include('cms.urls')),
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
