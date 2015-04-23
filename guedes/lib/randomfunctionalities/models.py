from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from solo.models import SingletonModel
from colorful.fields import RGBColorField


class Microformat(SingletonModel):
    """
    itemtype="http://schema.org/Person"
    http://microformats.org/wiki/hcard-authoring
    http://microformats.org/wiki/google-rich-snippets-examples
    """
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=100, blank=True)
    workplace = models.CharField(max_length=100, blank=True)
    thumb = FilerImageField(blank=True, null=True)  # django-solo required FilerImage to be null
    description = models.CharField(max_length=300, blank=True)
    last_update = models.DateField(blank=True, null=True)


ICON_CHOICES = [
    ['icon-facebook', _(u'Facebook')],
    # ['tw', _(u'Twitter')],
    ['icon-github', _(u'Github')],
    ['icon-linkedin', _(u'LinkedIn')],
    ['icon-youtube', _(u'Youtube')],
    ['icon-stackoverflow', _(u'Stackoverflow')],
    ['icon-soundcloud', _(u'Soundcloud')],
]


class Network(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    color = RGBColorField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    order = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
