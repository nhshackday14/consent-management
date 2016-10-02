# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.template.defaultfilters import slugify

class Migration(DataMigration):

    def forwards(self, orm):
        hernia = orm.Procedure(name="Inguinal Hernia Repair")
        hernia.slug = slugify(hernia.name)
        hernia.save()
        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        orm.Procedure.objects.filter(name="Inguinal Hernia Repair").delete()

    models = {
        u'consent_management.globalinfo': {
            'Meta': {'object_name': 'GlobalInfo'},
            'consultant_name': ('django.db.models.fields.TextField', [], {}),
            'how_to_get_there': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps_id': ('django.db.models.fields.CharField', [], {'default': "'ChIJz3g54adeeUgRMRGZkTY7BKk'", 'max_length': '32'})
        },
        u'consent_management.procedure': {
            'ICD9_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'Meta': {'object_name': 'Procedure'},
            'alternative_names': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'consent_form': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'procedure_details'", 'null': 'True', 'to': u"orm['consent_management.ProcedureDetails']"}),
            'extra_procedures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['consent_management.Procedure']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'consent_management.proceduredetails': {
            'Meta': {'object_name': 'ProcedureDetails'},
            'after_care': ('django.db.models.fields.TextField', [], {}),
            'anaesthesia': ('django.db.models.fields.TextField', [], {}),
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'follow_up': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recovery': ('django.db.models.fields.TextField', [], {}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['consent_management']
    symmetrical = True
