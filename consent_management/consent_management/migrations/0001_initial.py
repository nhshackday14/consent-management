# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConsentForm'
        db.create_table(u'consent_management_consentform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
            ('serious_risks', self.gf('django.db.models.fields.TextField')()),
            ('frequent_risks', self.gf('django.db.models.fields.TextField')()),
            ('intended_benefits', self.gf('django.db.models.fields.TextField')()),
            ('other_info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('references', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('patiant_info', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'consent_management', ['ConsentForm'])

        # Adding model 'Procedure'
        db.create_table(u'consent_management_procedure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('ICD9_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4)),
            ('consent_form', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='procedures', null=True, to=orm['consent_management.ConsentForm'])),
            ('alternative_names', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'consent_management', ['Procedure'])

        # Adding M2M table for field extra_procedures on 'Procedure'
        m2m_table_name = db.shorten_name(u'consent_management_procedure_extra_procedures')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_procedure', models.ForeignKey(orm[u'consent_management.procedure'], null=False)),
            ('to_procedure', models.ForeignKey(orm[u'consent_management.procedure'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_procedure_id', 'to_procedure_id'])


    def backwards(self, orm):
        # Deleting model 'ConsentForm'
        db.delete_table(u'consent_management_consentform')

        # Deleting model 'Procedure'
        db.delete_table(u'consent_management_procedure')

        # Removing M2M table for field extra_procedures on 'Procedure'
        db.delete_table(db.shorten_name(u'consent_management_procedure_extra_procedures'))


    models = {
        u'consent_management.consentform': {
            'Meta': {'object_name': 'ConsentForm'},
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'frequent_risks': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intended_benefits': ('django.db.models.fields.TextField', [], {}),
            'other_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'patiant_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'references': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'serious_risks': ('django.db.models.fields.TextField', [], {})
        },
        u'consent_management.procedure': {
            'ICD9_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'Meta': {'object_name': 'Procedure'},
            'alternative_names': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'consent_form': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'procedures'", 'null': 'True', 'to': u"orm['consent_management.ConsentForm']"}),
            'extra_procedures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['consent_management.Procedure']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['consent_management']