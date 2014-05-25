from django.db import models


class ConsentForm(models.Model):
    explanation = models.TextField(help_text="")
    serious_risks = models.TextField()
    frequent_risks = models.TextField()
    intended_benefits = models.TextField()
    other_info = models.TextField(blank=True)
    references = models.TextField(blank=True)
    patiant_info = models.TextField(blank=True)

    def __unicode__(self):
        procedures = ' | '.join(
            self.procedures.all().values_list('ICD9_code', flat=True))
        return u"ConsentForm for {}".format(procedures) if procedures \
            else u"Unused ConsentForm #{}".format(self.pk)


class Procedure(models.Model):
    name = models.CharField(
        max_length=255, null=False, unique=True
    )

    ICD9_code = models.CharField(
        max_length=4, null=False, unique=True
    )

    consent_form = models.ForeignKey(
        ConsentForm,
        related_name="procedures",
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
