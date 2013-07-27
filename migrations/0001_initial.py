# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Menu'
        db.create_table('mymenu_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
        ))
        db.send_create_signal('mymenu', ['Menu'])

        # Adding model 'MenuItems'
        db.create_table('mymenu_menuitems', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('target', self.gf('django.db.models.fields.CharField')(default='', max_length=10, null=True, blank=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['mymenu.Menu'])),
        ))
        db.send_create_signal('mymenu', ['MenuItems'])


    def backwards(self, orm):
        # Deleting model 'Menu'
        db.delete_table('mymenu_menu')

        # Deleting model 'MenuItems'
        db.delete_table('mymenu_menuitems')


    models = {
        'mymenu.menu': {
            'Meta': {'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'})
        },
        'mymenu.menuitems': {
            'Meta': {'object_name': 'MenuItems'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['mymenu.Menu']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'target': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mymenu']