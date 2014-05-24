from django.db import models


class ConsentForm(models.Model):
    alternative_names = models.TextField(
        blank=True,
        help_text="The proposed procedure. New lines delimiter"
    )
    explanation = models.TextField(
        help_text=""
    )
    serious_risks = models.TextField(
        help_text=""
    )
    frequent_risks = models.TextField(
        help_text=""
    )


class Procedure(models.Model):
    name = models.CharField(
        max_length=255, null=False, unique=True
    )
    consent_form = models.OneToOneField(
        ConsentForm,
        related_name="procedures",
        null=True
    )


class Chapter(models.Model):
    pass


class Blocks(models.Model):
    pass


class Categories(models.Model):
    pass
