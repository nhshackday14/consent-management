# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ConsentForm'
        db.delete_table(u'consent_management_consentform')

        # Adding model 'ProcedureDetails'
        db.create_table(u'consent_management_proceduredetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('anaesthesia', self.gf('django.db.models.fields.TextField')()),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
            ('recovery', self.gf('django.db.models.fields.TextField')()),
            ('follow_up', self.gf('django.db.models.fields.TextField')()),
            ('after_care', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'consent_management', ['ProcedureDetails'])

        # Adding model 'GlobalInfo'
        db.create_table(u'consent_management_globalinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consultant_name', self.gf('django.db.models.fields.TextField')()),
            ('maps_id', self.gf('django.db.models.fields.CharField')(default='ChIJz3g54adeeUgRMRGZkTY7BKk', max_length=32)),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'consent_management', ['GlobalInfo'])


        # Changing field 'Procedure.consent_form'
        db.alter_column(u'consent_management_procedure', 'consent_form_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['consent_management.ProcedureDetails']))

    def backwards(self, orm):
        # Adding model 'ConsentForm'
        db.create_table(u'consent_management_consentform', (
            ('references', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('frequent_risks', self.gf('django.db.models.fields.TextField')()),
            ('patiant_info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
            ('other_info', self.gf('django.db.models.fields.TextField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serious_risks', self.gf('django.db.models.fields.TextField')()),
            ('intended_benefits', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'consent_management', ['ConsentForm'])

        # Deleting model 'ProcedureDetails'
        db.delete_table(u'consent_management_proceduredetails')

        # Deleting model 'GlobalInfo'
        db.delete_table(u'consent_management_globalinfo')


        # Changing field 'Procedure.consent_form'
        db.alter_column(u'consent_management_procedure', 'consent_form_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['consent_management.ConsentForm']))

    models = {
        u'consent_management.globalinfo': {
            'Meta': {'object_name': 'GlobalInfo'},
            'consultant_name': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps_id': ('django.db.models.fields.CharField', [], {'default': "'ChIJz3g54adeeUgRMRGZkTY7BKk'", 'max_length': '32'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'consent_management.procedure': {
            'ICD9_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'Meta': {'object_name': 'Procedure'},
            'alternative_names': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'consent_form': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'procedure_details'", 'null': 'True', 'to': u"orm['consent_management.ProcedureDetails']"}),
            'extra_procedures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['consent_management.Procedure']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'consent_management.proceduredetails': {
            'Meta': {'object_name': 'ProcedureDetails'},
            'after_care': ('django.db.models.fields.TextField', [], {}),
            'anaesthesia': ('django.db.models.fields.TextField', [], {}),
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'follow_up': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recovery': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['consent_management']