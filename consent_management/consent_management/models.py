from django.db import models
from django.template.defaultfilters import slugify


class ProcedureDetails(models.Model):

    anaesthesia = models.TextField(null=True, blank=True)
    explanation = models.TextField(null=True, blank=True)
    recovery = models.TextField(null=True, blank=True)
    follow_up = models.TextField(null=True, blank=True)
    after_care = models.TextField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        procedures = ' | '.join(
            self.procedure_details.all().values_list('name', flat=True))
        return u"Procedure details for {}".format(procedures) if procedures \
            else u"Unused procedure details #{}".format(self.pk)


class GlobalInfo(models.Model):
    consultant_name = models.CharField(null=True, blank=True, max_length=256)
    maps_id = models.CharField(
        default="ChIJz3g54adeeUgRMRGZkTY7BKk", max_length=32,
        null=True, blank=True
    )
    how_to_get_there = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "#{} {}".format(self.consultant_name, self.maps_id)

class Procedure(models.Model):

    name = models.CharField(
        max_length=255, null=False, unique=True
    )

    slug = models.SlugField(
        max_length=255, null=False, unique=True
    )

    ICD9_code = models.CharField(
        max_length=4, null=False, unique=True
    )

    consent_form = models.OneToOneField(
        ProcedureDetails,
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Procedure, self).save(*args, **kwargs)

    def __unicode__(self):
        return "#{} {}".format(self.ICD9_code, self.name)
