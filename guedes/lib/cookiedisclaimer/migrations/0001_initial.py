# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CookieDisclaimer'
        db.create_table('cookiedisclaimer_cookiedisclaimer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_pt', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('cookiedisclaimer', ['CookieDisclaimer'])


    def backwards(self, orm):
        # Deleting model 'CookieDisclaimer'
        db.delete_table('cookiedisclaimer_cookiedisclaimer')


    models = {
        'cookiedisclaimer.cookiedisclaimer': {
            'Meta': {'object_name': 'CookieDisclaimer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_pt': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cookiedisclaimer']