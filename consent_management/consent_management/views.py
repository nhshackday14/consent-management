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
