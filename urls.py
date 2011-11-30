# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from fblog.sitemap import BlogSitemap
from django.contrib.sitemaps import FlatPageSitemap

class MyFlatPageSitemap(FlatPageSitemap):
    def priority(self, item):
        return 0.5

sitemaps = {
    'blog': BlogSitemap,
    'pages': MyFlatPageSitemap,
}

urlpatterns = patterns('',
    #(r'^$', direct_to_template, {'template':'base.html'}),
    (r'^', include('fprice.urls')),
    (r'^blog/', include('fblog.urls')),

    (r'^accounts/', include('registration.urls')),
    (r'^favorites/', include('favorites.urls', app_name='favorites', namespace="favorites")),

    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^comments/', include('django.contrib.comments.urls')),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^yandex_417e26a084231734.html$', 'django.views.static.serve', {'path':"/yandex_master.html",'document_root': settings.STATIC_ROOT,'show_indexes': False}),
)

# routing static files
if settings.LOCALSERVER:
    urlpatterns+= patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )
