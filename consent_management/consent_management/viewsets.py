from django.db.models.query_utils import Q

from rest_framework import viewsets
from rest_framework.response import Response

from consent_management.serializers import (
    ProcedureSerializer
)

from consent_management.models import Procedure


class ProcedureViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows projects to be viewed.
    """
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

    def list(self, request):
        query_params = request.GET.get('q')
        queryset = Procedure.objects.all()
        if query_params:
            Q1 = Q(name__icontains=query_params)
            Q2 = Q(alternative_names__icontains=query_params)
            queryset = queryset.filter(Q1 | Q2)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
