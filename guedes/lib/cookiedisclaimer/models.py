# -*- coding: utf-8 -*- #
from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel


class CookieDisclaimer(SingletonModel):
    text = models.TextField(default="I've set a cookie so that I could notify you of it using this cookie notification bar. You're welcome.")
    accept_text = models.CharField(max_length=100, default='Nice bamboozle. Cheers!')
    decline_text = models.CharField(max_length=100, default='0/10 no https. Let me out')
    back_url = models.URLField(default='http://livepuppycam.com/')

    class Meta:
        verbose_name_plural = _(u"Cookie Disclaimer")

    def __str__(self):
        return self.text[:50]
