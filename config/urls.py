# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

# import service.kernel.urls

# import service.frontend.views

urlpatterns = (
    # url(r'^', include('service.frontend.urls')),

    url(r'^api/', include('service.kernel.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if settings.DEBUG:
    # url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),

    if ('debug_toolbar' in settings.INSTALLED_APPS):
        import debug_toolbar

        urlpatterns += (url(r'^__debug__/', include(debug_toolbar.urls)),)
else:
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permissin Denied")}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
    ]