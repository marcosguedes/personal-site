from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from django.core.urlresolvers import reverse
import datetime

class PostManager(models.Manager):
    use_for_related_fields = True

    def published(self):
        return super(PostManager, self).filter(published=True)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_related_posts(self):
        return self.posts.published()

class Post(models.Model):
    published = models.BooleanField(verbose_name=_(u"Published"), default=True)
    title = models.CharField(verbose_name=_(u"Title"), max_length=200)
    slug = models.SlugField(verbose_name=_(u"Slug"), max_length=200, unique=True)
    date_created = models.DateField(verbose_name=_(u"Date Created"), default=datetime.date.today)
    tags = models.ManyToManyField(Tag, verbose_name=_(u"Tags"), blank=True, related_name="posts")

    objects = PostManager()

    class Meta:
        verbose_name = _(u"Post")
        verbose_name_plural = _(u"Posts")
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_tags(self):
        return self.tags.all()

    def get_content(self):
        return self.content.all()
    
    # def get_absolute_url(self):
    #     return reverse()


class Content(models.Model):
    post = models.ForeignKey(Post, related_name="content")
    image = FilerImageField(verbose_name=_(u"Image"), blank=True, null=True)
    text = RichTextField(verbose_name=_(u"Text"), blank=True)
    order = models.SmallIntegerField(verbose_name=_(u"Order"), default=0)

    class Meta:
        ordering = ['order']
