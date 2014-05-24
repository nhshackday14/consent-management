from rest_framework import serializers

from consent_management import models


class ConsentFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ConsentForm


class ProcedureSerializer(serializers.ModelSerializer):

    consent_form = ConsentFormSerializer()

    class Meta:
        model = models.Procedure
        fields = ('name', 'consent_form',)
