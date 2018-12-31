from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from solo.models import SingletonModel
from django.core.urlresolvers import reverse


class HomePage(SingletonModel):
    text = RichTextField(config_name='default')

    def get_absolute_url(self):
        return reverse("page:home")


class AboutPage(SingletonModel):
    picture = FilerImageField(blank=True, null=True)
    text = RichTextField(config_name='default')

    def get_absolute_url(self):
        return reverse("page:about")
