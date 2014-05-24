from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from consent_management.viewsets import (
    ProcedureViewSet
)

router = routers.DefaultRouter()
router.register(r'procedures', ProcedureViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'consent_management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
