# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        hernia, _ = orm.Procedure.objects.get_or_create(name="Inguinal Hernia Repair")
        hernia.save()
        details = orm.ProcedureDetails()

        details.anaesthesia = """
Your child will be given a general anaesthetic, which means that he or she will
be asleep for the operation. Your child will normally be able to go home the
same day.

Your child may be given a local anaesthetic before he or she wakes up, either
by injection or by gel applied to the area. This means that he or she will feel
less pain immediately after the operation
        """

        details.explanation = """
The operation is done through a small incision made along the groin crease
(which will leave a small scar). The aim of an inguinal hernia repair operation
is to push the hernia sac back into place and strengthen the abdominal wall. To
strengthen the area of weakness, the surgeon will often stitch in place a piece
of artificial mesh, made from polypropylene.

The doctor may examine the opposite groin to see if there is a hernia there as
well.


        """

        details.recovery = """
Your child will be monitored for a short while and then brought back to the
ward to recover. He or she may be sleepy, and feel or be sick. It's possible
that your child will be upset after the procedure. He or she will need to rest
until the effects of the general anaesthetic have passed. Your child should be
able to eat and drink soon after the operation.

Once your child is comfortable and eating and drinking, he or she will be able
to go home. This is likely to be around three to four hours after the operation.
 However, if your child is under three months old, he or she will probably be
kept in hospital overnight for monitoring.

Your child's surgeon may prescribe antibiotics for a few days, although this is
unusual. If your child is prescribed antibiotics, it's important that he or she
finishes the course
        """

        details.follow_up = """
Your child will be seen again in the outpatient department, generally four to
six weeks after the operation. This will be arranged by the nurse or the
consultant's secretary.
        """

        details.after_care = """
Contact Starfish Ward or your nearest Accident and Emergency department for
advice if you notice any of the following:

1. Your child complains of severe pain or shows signs of worsening pain - young
children cry more
2. When they are in pain and are often difficult to settle
3. Your child develops a temperature
4. The wound is red, swollen, bleeding or has a discharg


### Stitches ###

The stitches are hidden in the wound and will dissolve on their own.

### Dressing ###

If your child has a dressing over the wound or if Steri-Strips (paper strips)
were used, you can remove them in the bath after three days. If the area around
the wound becomes dirty, you can remove the dressing sooner. In most cases your
child will not need a new dressing.

### Bathing ###

Your child can have a bath as usual.

### Clothing ###

Loose clothing is advised until the wound is fully healed.

Your child may need to take a few days off school and shouldn't ride a bike or
swim for at least two weeks

        """

        details.save()
        hernia.consent_form = details
        hernia.save()


    def backwards(self, orm):
        "Write your backwards methods here."
        hernia, _ = orm.Procedure.objects.get_or_create(name="Inguinal Hernia Repair")
        hernia.save()
        details = hernia.consent_form
        details.delete()

    models = {
        u'consent_management.globalinfo': {
            'Meta': {'object_name': 'GlobalInfo'},
            'consultant_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'how_to_get_there': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps_id': ('django.db.models.fields.CharField', [], {'default': "'ChIJz3g54adeeUgRMRGZkTY7BKk'", 'max_length': '32', 'null': 'True', 'blank': 'True'})
        },
        u'consent_management.procedure': {
            'ICD9_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'Meta': {'object_name': 'Procedure'},
            'alternative_names': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'consent_form': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['consent_management.ProcedureDetails']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'extra_procedures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['consent_management.Procedure']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'consent_management.proceduredetails': {
            'Meta': {'object_name': 'ProcedureDetails'},
            'after_care': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'anaesthesia': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'explanation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'follow_up': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recovery': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['consent_management']
    symmetrical = True
