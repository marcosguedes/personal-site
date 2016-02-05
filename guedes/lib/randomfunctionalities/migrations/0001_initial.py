# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Microformat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('workplace', models.CharField(max_length=100, blank=True)),
                ('description', models.CharField(max_length=300, blank=True)),
                ('last_update', models.DateField(null=True, blank=True)),
                ('thumb', filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('color', colorful.fields.RGBColorField()),
                ('icon', models.CharField(max_length=50, choices=[[b'icon-facebook', 'Facebook'], [b'icon-github', 'Github'], [b'icon-linkedin', 'LinkedIn'], [b'icon-youtube', 'Youtube'], [b'icon-stackoverflow', 'Stackoverflow'], [b'icon-soundcloud', 'Soundcloud']])),
                ('order', models.SmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
            },
        ),
    ]
