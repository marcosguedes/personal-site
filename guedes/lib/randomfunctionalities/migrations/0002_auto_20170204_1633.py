# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomfunctionalities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='icon',
            field=models.CharField(max_length=50, choices=[['icon-facebook', 'Facebook'], ['icon-github', 'Github'], ['icon-linkedin', 'LinkedIn'], ['icon-youtube', 'Youtube'], ['icon-stackoverflow', 'Stackoverflow'], ['icon-soundcloud', 'Soundcloud']]),
        ),
    ]
