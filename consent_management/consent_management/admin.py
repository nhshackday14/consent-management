from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from consent_management.models import Procedure, ProcedureDetails, GlobalInfo


class ProcedureFormAdmin(forms.ModelForm):

    extra_procedures = forms.ModelMultipleChoiceField(
        queryset=Procedure.objects.all(),
        widget=FilteredSelectMultiple(
            "Other procedures that share this consent form",
            is_stacked=False
        ),
        required=False,
    )


class ProcedureAdmin(admin.ModelAdmin):

    form = ProcedureFormAdmin
    search_fields = ['name']


admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(ProcedureDetails)
admin.site.register(GlobalInfo)
