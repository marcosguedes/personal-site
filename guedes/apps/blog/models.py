from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from django.core.urlresolvers import reverse
import datetime
from django.utils.text import slugify
from django.utils import timezone
from bakery.models import BuildableModel

class PostManager(models.Manager):
    use_for_related_fields = True

    def published(self):
        return super(PostManager, self).filter(published=True)


class Tag(BuildableModel):
    detail_views = ('blog.views.TagPostListView',)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name
    
    def get_related_posts(self):
        return self.posts.published()

    def get_absolute_url(self):
        return reverse("blog:tag_post_list", kwargs = {"slug": self.slug})

class Post(BuildableModel):
    detail_views = ('blog.views.PostDetailView',)
    published = models.BooleanField(verbose_name=_(u"Published"), default=True)
    title = models.CharField(verbose_name=_(u"Title"), max_length=200)
    slug = models.SlugField(verbose_name=_(u"Slug"), max_length=200, unique=True)
    text = models.TextField(verbose_name=_(u"Text"))
    date_created = models.DateTimeField(verbose_name=_(u"Date Created"), default=timezone.now)
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

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
