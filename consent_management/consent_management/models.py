from django.db import models


class ConsentForm(models.Model):
    procedure_name = models.CharField(
        max_length=255, null=False, unique=True,
        help_text="Name of proposed procedure or course of treatment"
    )
    alternative_names = models.CharField(
        max_length=255, null=False,
        help_text="The proposed procedure"
    )
    explanation = models.CharField(
        max_length=255,
        help_text=""
    )
    serious_risks = models.CharField(
        max_length=255,
        help_text=""
    )
    frequent_risks = models.CharField(
        max_length=255,
        help_text=""
    )


class Chapter(models.Model):
    pass


class Blocks(models.Model):
    pass


class Categories(models.Model):
    pass
