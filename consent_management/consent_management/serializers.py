from rest_framework.serializers import ModelSerializer, SerializerMethodField

from consent_management import models


class ConsentFormSerializer(ModelSerializer):
    class Meta:
        model = models.ProcedureDetails


class ProcedureSerializer(ModelSerializer):
    consent_form = ConsentFormSerializer()
    alternative_names = SerializerMethodField('get_alternative_names_list')
    extra_procedures = SerializerMethodField('get_verbose_extra_procedures')

    def get_alternative_names_list(self, obj):
        return obj.alternative_names.replace('\r', '').split('\n') \
            if obj.alternative_names else []

    def get_verbose_extra_procedures(self, obj):
        return obj.extra_procedures.all().values('name', 'id',)

    class Meta:
        model = models.Procedure
