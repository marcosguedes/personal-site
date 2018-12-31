from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt', include('robots.urls')),
    url(r'^humans\.txt', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^', include('personalsite.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
