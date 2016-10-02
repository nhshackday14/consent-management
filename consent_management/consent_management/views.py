from django.views.generic import DetailView, TemplateView
from consent_management import models


class IndexView(TemplateView):
    template_name = 'index.html'


class ProcedureDetailView(DetailView):
    """
    Failover view for templates - just look for this path in Django!
    """
    model = models.Procedure
    template_name = "templates/procedure.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super(ProcedureDetailView, self).get_context_data(*args, **kwargs)
        ctx["md"] = """
Inguinal Hernia Repair
======================

Anaesthesia
-----------

Your child will be given a general anaesthetic, which means that he or she will
be asleep for the operation. Your child will normally be able to go home the
same day.

Your child may be given a local anaesthetic before he or she wakes up, either
by injection or by gel applied to the area. This means that he or she will feel
less pain immediately after the operation.

Explanation
-----------

The operation is done through a small incision made along the groin crease
(which will leave a small scar). The aim of an inguinal hernia repair operation
is to push the hernia sac back into place and strengthen the abdominal wall. To
strengthen the area of weakness, the surgeon will often stitch in place a piece
of artificial mesh, made from polypropylene.

The doctor may examine the opposite groin to see if there is a hernia there as
well.

Recovery
--------

Your child will be monitored for a short while and then brought back to the
ward to recover. He or she may be sleepy, and feel or be sick. It's possible
that your child will be upset after the procedure. He or she will need to rest
until the effects of the general anaesthetic have passed. Your child should be
able to eat and drink soon after the operation.

Once your child is comfortable and eating and drinking, he or she will be able
to go home. This is likely to be around three to four hours after the operation.
 However, if your child is under three months old, he or she will probably be
kept in hospital overnight for monitoring.
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
Your child's surgeon may prescribe antibiotics for a few days, although this is
unusual. If your child is prescribed antibiotics, it's important that he or she
finishes the course.

### Pain relief ###

You can give your child over-the-counter painkillers such as paracetamol or
ibuprofen syrup (for example, Calpol or Calprofen) regularly for the first 24
to 48 hours. Follow the instructions on the leaflet that comes with the
medicine and ask your pharmacist for advice. Do not give aspirin to children
under 16 years old.

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
swim for at least two weeks.

Followup
--------

Your child will be seen again in the outpatient department, generally four to
six weeks after the operation. This will be arranged by the nurse or the
consultant's secretary.

Aftercare
---------

Contact Starfish Ward or your nearest Accident and Emergency department for
advice if you notice any of the following:

 1. Your child complains of severe pain or shows signs of worsening pain - young
  children cry more
 2. When they are in pain and are often difficult to settle
 3. Your child develops a temperature
 4. The wound is red, swollen, bleeding or has a discharge

 ### Contact ###

 With these, or any other concerns, contact Starfish Ward directly on
 +44 (0)20 7460 5991 and you will be able to speak to a paediatric nurse
 or a doctor."""
        ctx["md"] = ctx["md"].encode('ascii', 'ignore')
        return ctx
