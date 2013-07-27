# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'MenuItems'
        db.delete_table('mymenu_menuitems')

        # Adding model 'MenuItem'
        db.create_table('mymenu_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('target', self.gf('django.db.models.fields.CharField')(default='', max_length=10, null=True, blank=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['mymenu.Menu'])),
        ))
        db.send_create_signal('mymenu', ['MenuItem'])


    def backwards(self, orm):
        # Adding model 'MenuItems'
        db.create_table('mymenu_menuitems', (
            ('target', self.gf('django.db.models.fields.CharField')(default='', max_length=10, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['mymenu.Menu'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('mymenu', ['MenuItems'])

        # Deleting model 'MenuItem'
        db.delete_table('mymenu_menuitem')


    models = {
        'mymenu.menu': {
            'Meta': {'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'})
        },
        'mymenu.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['mymenu.Menu']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'target': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mymenu']