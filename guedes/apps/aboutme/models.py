from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from django.core.urlresolvers import reverse


class InterestManager(models.Manager):
    use_for_related_fields = True

    def active(self):
        return super(InterestManager, self).filter(active=True)


class CommonAttributesMixin(models.Model):
    active = models.BooleanField(default=True)
    order = models.SmallIntegerField(default=0)
    title = models.CharField(max_length=100, blank=True)

    objects = InterestManager()

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['order']


class Category(CommonAttributesMixin):
    slug = models.SlugField(max_length=100, blank=True)
    short_description = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name_plural = _(u"Categories")
        ordering = ['order']

    def get_items(self):
        return self.items.filter(active=True)


class Interest(CommonAttributesMixin):
    category = models.ForeignKey(Category, related_name="items")
    image = FilerImageField(blank=True, null=True)
    description = RichTextField(config_name='default', blank=True)
    slug = models.SlugField(max_length=100)

    objects = InterestManager()

    class Meta:
        ordering = ['order']

    def get_absolute_url(self):
        return reverse("interest_detail", kwargs={"slug": self.slug})
