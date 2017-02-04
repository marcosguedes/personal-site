# -*- coding: utf-8 -*- #
from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel


class CookieDisclaimer(SingletonModel):
    text = models.TextField()

    class Meta:
        verbose_name_plural = _(u"Cookie Disclaimer")

    def __str__(self):
        return self.text[:50]
