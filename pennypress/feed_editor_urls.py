from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)', 'pennypress.feed_editor_views.bootstrap', name='feed_editor_static'),
    url(r'^$', 'pennypress.feed_editor_views.feed_editor', name='feed_editor'),
)
