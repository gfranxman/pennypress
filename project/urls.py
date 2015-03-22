from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pennypress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^feed_editor/', include('pennypress.feed_editor_urls')),
    url(r'^feed/(?P<feed_slug>[^/]+)', 'pennypress.views.feed_view', name='feed_view'),

    # commonly requested url we dont care about
    url(r'^favicon.ico$',"project.views.go_away", name="favicon-icon-redirect"),
    url(r'^apple-touch-icon.*.png$', "project.views.go_away", name="safari-icon-redirect"),

    # section, last because its a wildcard for now
    url(r'^(?P<slug>.+)/$', 'pennypress.views.section', name='section'),
)
