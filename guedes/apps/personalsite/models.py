from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from solo.models import SingletonModel


class HomePage(SingletonModel):
    page_title = models.CharField(max_length=300, default='Marcos Guedes')
    # meta_description = models.CharField(max_length=300, blank=True)
    picture = FilerImageField(blank=True, null=True)  # django-solo required FilerImage to be null
    text = RichTextField(config_name='default')

    def get_absolute_url(self):
        return '/'  # needed for bakery
