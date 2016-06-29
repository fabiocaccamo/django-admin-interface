# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Theme'
        db.create_table(u'admin_interface_theme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Django', max_length=50)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Django administration', max_length=50, blank=True)),
            ('title_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('logo', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('logo_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('css_header_background_color', self.gf('colorfield.fields.ColorField')(default='#0C4B33', max_length=10, blank=True)),
            ('css_header_title_color', self.gf('colorfield.fields.ColorField')(default='#F5DD5D', max_length=10, blank=True)),
            ('css_header_text_color', self.gf('colorfield.fields.ColorField')(default='#44B78B', max_length=10, blank=True)),
            ('css_header_link_color', self.gf('colorfield.fields.ColorField')(default='#FFFFFF', max_length=10, blank=True)),
            ('css_header_link_hover_color', self.gf('colorfield.fields.ColorField')(default='#C9F0DD', max_length=10, blank=True)),
            ('css_module_background_color', self.gf('colorfield.fields.ColorField')(default='#44B78B', max_length=10, blank=True)),
            ('css_module_text_color', self.gf('colorfield.fields.ColorField')(default='#FFFFFF', max_length=10, blank=True)),
            ('css_module_link_color', self.gf('colorfield.fields.ColorField')(default='#FFFFFF', max_length=10, blank=True)),
            ('css_module_link_hover_color', self.gf('colorfield.fields.ColorField')(default='#C9F0DD', max_length=10, blank=True)),
            ('css_module_rounded_corners', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('css_generic_link_color', self.gf('colorfield.fields.ColorField')(default='#0C3C26', max_length=10, blank=True)),
            ('css_generic_link_hover_color', self.gf('colorfield.fields.ColorField')(default='#156641', max_length=10, blank=True)),
            ('css_save_button_background_color', self.gf('colorfield.fields.ColorField')(default='#0C4B33', max_length=10, blank=True)),
            ('css_save_button_background_hover_color', self.gf('colorfield.fields.ColorField')(default='#0C3C26', max_length=10, blank=True)),
            ('css_save_button_text_color', self.gf('colorfield.fields.ColorField')(default='#FFFFFF', max_length=10, blank=True)),
            ('css_delete_button_background_color', self.gf('colorfield.fields.ColorField')(default='#BA2121', max_length=10, blank=True)),
            ('css_delete_button_background_hover_color', self.gf('colorfield.fields.ColorField')(default='#A41515', max_length=10, blank=True)),
            ('css_delete_button_text_color', self.gf('colorfield.fields.ColorField')(default='#FFFFFF', max_length=10, blank=True)),
            ('css', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('list_filter_dropdown', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('admin_interface', ['Theme'])


    def backwards(self, orm):
        # Deleting model 'Theme'
        db.delete_table(u'admin_interface_theme')


    models = {
        'admin_interface.theme': {
            'Meta': {'object_name': 'Theme'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'css': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'css_delete_button_background_color': ('colorfield.fields.ColorField', [], {'default': "'#BA2121'", 'max_length': '10', 'blank': 'True'}),
            'css_delete_button_background_hover_color': ('colorfield.fields.ColorField', [], {'default': "'#A41515'", 'max_length': '10', 'blank': 'True'}),
            'css_delete_button_text_color': ('colorfield.fields.ColorField', [], {'default': "'#FFFFFF'", 'max_length': '10', 'blank': 'True'}),
            'css_generic_link_color': ('colorfield.fields.ColorField', [], {'default': "'#0C3C26'", 'max_length': '10', 'blank': 'True'}),
            'css_generic_link_hover_color': ('colorfield.fields.ColorField', [], {'default': "'#156641'", 'max_length': '10', 'blank': 'True'}),
            'css_header_background_color': ('colorfield.fields.ColorField', [], {'default': "'#0C4B33'", 'max_length': '10', 'blank': 'True'}),
            'css_header_link_color': ('colorfield.fields.ColorField', [], {'default': "'#FFFFFF'", 'max_length': '10', 'blank': 'True'}),
            'css_header_link_hover_color': ('colorfield.fields.ColorField', [], {'default': "'#C9F0DD'", 'max_length': '10', 'blank': 'True'}),
            'css_header_text_color': ('colorfield.fields.ColorField', [], {'default': "'#44B78B'", 'max_length': '10', 'blank': 'True'}),
            'css_header_title_color': ('colorfield.fields.ColorField', [], {'default': "'#F5DD5D'", 'max_length': '10', 'blank': 'True'}),
            'css_module_background_color': ('colorfield.fields.ColorField', [], {'default': "'#44B78B'", 'max_length': '10', 'blank': 'True'}),
            'css_module_link_color': ('colorfield.fields.ColorField', [], {'default': "'#FFFFFF'", 'max_length': '10', 'blank': 'True'}),
            'css_module_link_hover_color': ('colorfield.fields.ColorField', [], {'default': "'#C9F0DD'", 'max_length': '10', 'blank': 'True'}),
            'css_module_rounded_corners': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'css_module_text_color': ('colorfield.fields.ColorField', [], {'default': "'#FFFFFF'", 'max_length': '10', 'blank': 'True'}),
            'css_save_button_background_color': ('colorfield.fields.ColorField', [], {'default': "'#0C4B33'", 'max_length': '10', 'blank': 'True'}),
            'css_save_button_background_hover_color': ('colorfield.fields.ColorField', [], {'default': "'#0C3C26'", 'max_length': '10', 'blank': 'True'}),
            'css_save_button_text_color': ('colorfield.fields.ColorField', [], {'default': "'#FFFFFF'", 'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_filter_dropdown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'logo_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Django'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Django administration'", 'max_length': '50', 'blank': 'True'}),
            'title_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['admin_interface']