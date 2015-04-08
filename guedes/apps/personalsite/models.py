from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class HomePage(models.Model):
    page_title = models.CharField(_(u"Text Title"), max_length=300, blank=True)
    meta_description = models.CharField(_(u"Text Title"), max_length=300, blank=True)
    picture = FilerImageField()
    text = RichTextField(config_name='default')
    facebook_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
