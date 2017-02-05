# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('order', models.SmallIntegerField(verbose_name='Order', default=0)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', blank=True, null=True, verbose_name='Image')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('published', models.BooleanField(verbose_name='Published', default=True)),
                ('title', models.CharField(verbose_name='Title', max_length=200)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=200, unique=True)),
                ('date_created', models.DateField(verbose_name='Date Created', default=datetime.date.today)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(verbose_name='Tags', related_name='posts', blank=True, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='content',
            name='post',
            field=models.ForeignKey(to='blog.Post', related_name='content'),
        ),
    ]
