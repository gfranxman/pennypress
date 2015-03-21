from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pennypress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # commonly requested url we dont care about
    url(r'^favicon.ico$',"project.views.go_away", name="favicon-icon-redirect"),
    url(r'^apple-touch-icon.*.png$', "project.views.go_away", name="safari-icon-redirect"),

    # section, last because its a wildcard for now
    url(r'^(?P<slug>.+)/$', 'pennypress.views.section', name='section'),
)
