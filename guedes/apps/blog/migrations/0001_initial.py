# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('order', models.SmallIntegerField(default=0, verbose_name='Order')),
                ('image', filer.fields.image.FilerImageField(verbose_name='Image', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.BooleanField(default=True, verbose_name='Published')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('date_created', models.DateField(default=datetime.date.today, verbose_name='Date Created')),
            ],
            options={
                'ordering': ['date_created'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', verbose_name='Tags', to='blog.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='content',
            name='post',
            field=models.ForeignKey(related_name='content', to='blog.Post'),
        ),
    ]
