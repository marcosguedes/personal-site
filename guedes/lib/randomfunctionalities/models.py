from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from solo.models import SingletonModel


class Microformat(SingletonModel):
    """
    itemtype="http://schema.org/Person"
    http://microformats.org/wiki/hcard-authoring
    http://microformats.org/wiki/google-rich-snippets-examples
    """
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=100, blank=True)
    workplace = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)
    thumb = FilerImageField(blank=True, null=True)  # django-solo required FilerImage to be null
    description = models.CharField(max_length=300, blank=True)
    last_update = models.DateField()
