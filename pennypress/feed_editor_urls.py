from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)', 'pennypress.feed_editor_views.bootstrap', name='feed_editor_static'),
    url(r'^(?P<feed_slug>.*)/reset_sortkey_for_feeditem/(?P<feeditem_id>.*)/', 'pennypress.feed_editor_views.reset_sortkey_for_feeditem', name='reset_sortkey_for_feeditem'),
    url(r'^(?P<feed_slug>.*)/$', 'pennypress.feed_editor_views.feed_editor', name='feed_editor'),
    url(r'^$', 'pennypress.feed_editor_views.feed_editor', {'feed_slug':'local'}, name='feed_editor_home'),
)
