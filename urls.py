# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from sitemaps import sitemaps

urlpatterns = patterns('',
    #(r'^$', direct_to_template, {'template':'fprice/home.html'}, 'home'),
    url("^$", "django.contrib.flatpages.views.flatpage", {"url": "/"}, name="home"),
    #(r'^blog/', include('fblog.urls')),

    (r'^accounts/', include('registration.urls')),
    #(r'^profiles/', include('profiles.urls')),
    #(r'^favorites/', include('favorites.urls', app_name='favorites', namespace="favorites")),

    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^comments/', include('django.contrib.comments.urls')),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^yandex_417e26a084231734.html$', 'django.views.static.serve', {'path':"/yandex_master.html",'document_root': settings.STATIC_ROOT,'show_indexes': False}),
)

# routing media files
if settings.LOCALSERVER:
    urlpatterns+= patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns+= patterns('',
    (r'^', include('fprice.urls')), # sad / but true
)
