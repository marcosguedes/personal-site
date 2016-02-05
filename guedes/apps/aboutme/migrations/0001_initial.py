# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('slug', models.SlugField(max_length=100, blank=True)),
                ('short_description', models.CharField(max_length=300, blank=True)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('order', models.SmallIntegerField(default=0)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('slug', models.SlugField(max_length=100)),
                ('category', models.ForeignKey(related_name='items', to='aboutme.Category')),
                ('image', filer.fields.image.FilerImageField(related_name='interest_image', blank=True, to='filer.Image', null=True)),
                ('thumbnail', filer.fields.image.FilerImageField(related_name='interest_thumb', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
