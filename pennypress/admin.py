from django.contrib import admin

from pennypress.models import *

'''
# Register your models here.
class BaseAuditable( models.Model ):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="%(app_label)s_%(class)s_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="%(app_label)s_%(class)s_updater")
    class Meta:
class TagAdmin( BaseAuditable ):
class SectionAdmin( BaseAuditable ):
class BasePublishable( BaseAuditable ):
    class Meta:
class PhotoAdmin( BasePublishable ):
class StoryAdmin( BasePublishable ):
class VideoAdmin( BasePublishable ):
class LinkAdmin( BaseAuditable ):
class PointAdmin( BaseAuditable ):
class PlaceAdmin( Point ):
class StateAdmin( BaseAuditable ):
class CountyAdmin( BaseAuditable ):
class CityAdmin( BaseAuditable ):
class ZipCodeAdmin( BaseAuditable ):
class AddressAdmin( Place ):
class DatelineAdmin( BaseAuditable ):
class OrganizationAdmin( Address ):
class SchoolAdmin( Organization ):
class ParkAdmin( Address ):
class ChurchAdmin( Organization ):
class PollingStationAdmin( Address ):
class SportAdmin( BaseAuditable ):
class EventTemplateAdmin( BaseAuditable ):
class EventAdmin( BaseAuditable ):
'''
admin.site.register( Tag )
admin.site.register( Section )
admin.site.register( Story )
admin.site.register( Photo )
admin.site.register( Video )
admin.site.register( Link )
admin.site.register( Point )
admin.site.register( Place )
admin.site.register( City )
admin.site.register( State )
admin.site.register( County )
admin.site.register( ZipCode )
admin.site.register( Address )
admin.site.register( Dateline )
admin.site.register( Organization )
admin.site.register( Park )
admin.site.register( Church )
admin.site.register( PollingStation )
admin.site.register( Sport )
admin.site.register( EventType )
admin.site.register( EventTemplate )
admin.site.register( Event )
admin.site.register( StreamType )
admin.site.register( Stream )
admin.site.register( Item )
admin.site.register( Feed )
admin.site.register( FeedItem )

