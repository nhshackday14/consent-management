from django.db import models


class ProcedureDetails(models.Model):

    name = models.CharField(max_length=255)
    anaesthesia = models.TextField()
    explanation = models.TextField()
    recovery = models.TextField()
    follow_up = models.TextField()
    after_care = models.TextField()

    def __unicode__(self):
        procedures = ' | '.join(
            self.procedure_details.all().values_list('name', flat=True))
        return u"Procedure details for {}".format(procedures) if procedures \
            else u"Unused procedure details #{}".format(self.pk)


class GlobalInfo(models.Model):

    consultant_name = models.TextField()
    maps_id = models.CharField(default="ChIJz3g54adeeUgRMRGZkTY7BKk",max_length=32)
    video_url = models.URLField()

    def __unicode__(self):
        return "#{} {} {}".format(self.consultant_name, self.maps_id,self.video_url)

class Procedure(models.Model):

    name = models.CharField(
        max_length=255, null=False, unique=True
    )

    ICD9_code = models.CharField(
        max_length=4, null=False, unique=True
    )

    consent_form = models.ForeignKey(
        ProcedureDetails,
        related_name="procedure_details",
        null=True,
        blank=True,
    )

    alternative_names = models.TextField(
        blank=True,
        help_text="Alternative names of the procedure. New lines delimiter"
    )

    extra_procedures = models.ManyToManyField(
        'Procedure', null=True, blank=True)

    def get_alternative_names_list(self):
        return self.alternative_names.split('\n')

    def __unicode__(self):
        return "#{} {}".format(self.ICD9_code, self.name)
