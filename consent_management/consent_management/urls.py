from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from consent_management.viewsets import (
    ProcedureViewSet
)
from consent_management.views import IndexView, ProcedureDetailView

router = routers.DefaultRouter()
router.register(r'procedures', ProcedureViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^procedure/(?P<slug>[-\w]+)$', ProcedureDetailView.as_view(), name='procedure-detail'),
)
