# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

admin.autodiscover()

# urlpatterns = i18n_patterns('',
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^', include('cms.urls')),
]

# # This is only needed when using runserver.
# if settings.DEBUG:
#     urlpatterns = [
#         url(r'^media/(?P<path>.*)$', serve,  # NOQA
#             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#         ] + staticfiles_urlpatterns() + urlpatterns  # NOQA
