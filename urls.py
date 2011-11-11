from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template
from fblog.sitemap import BlogSitemap

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = patterns('',
    #(r'^$', direct_to_template, {'template':'base.html'}),
    (r'^', include('fprice.urls')),
    (r'^blog/', include('fblog.urls')),

    (r'^accounts/', include('registration.urls')),

    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^comments/', include('django.contrib.comments.urls')),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

# routing static files
from django.conf import settings
if settings.LOCALSERVER:
    urlpatterns+= patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )
