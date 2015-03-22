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
'''
class Photo( BasePublishable ):
    class Story( BasePublishable ):
    class Video( BasePublishable ):
    class Item( BasePublishable ):
    class Feed( BasePublishable ):
'''
class AuditAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    save_on_top = True # doesnt seem to work
    readonly_fields = ("created_date","updated_date",)

class PublishableAdmin( AuditAdmin ):
    date_hierarchy = 'pub_date'
    search_fields = ( 'title', 'subtitle', 'slug', 'tags__slug', 'authors__email', 'authors__username', 'authors__last_name' )

#class ProductAdmin(AuditAdmin):
#    list_display = ('name', 'sku', 'application','for_sale', 'family', 'payment_system', 'renewal_frequency'  )
#    list_filter = ( 'for_sale', 'application', 'family', 'payment_system__enabled', 'renewal_frequency' )
#    search_fields = ( 'name', 'application__name', 'application__app_id', 'sku' )
#    
#admin.site.register(Product, ProductAdmin)


admin.site.register( Tag, AuditAdmin )
admin.site.register( Section, AuditAdmin )
admin.site.register( Story, PublishableAdmin )
admin.site.register( Photo, PublishableAdmin )
admin.site.register( Video, PublishableAdmin )
admin.site.register( Link, AuditAdmin )
admin.site.register( Point, AuditAdmin )
admin.site.register( Place, AuditAdmin )
admin.site.register( City, AuditAdmin )
admin.site.register( State, AuditAdmin )
admin.site.register( County, AuditAdmin )
admin.site.register( ZipCode, AuditAdmin )
admin.site.register( Address, AuditAdmin )
admin.site.register( Dateline, AuditAdmin )
admin.site.register( Organization, AuditAdmin )
admin.site.register( Park, AuditAdmin )
admin.site.register( Church, AuditAdmin )
admin.site.register( PollingStation, AuditAdmin )
admin.site.register( Sport, AuditAdmin )
admin.site.register( EventType, AuditAdmin )
admin.site.register( EventTemplate, AuditAdmin )
admin.site.register( Event, AuditAdmin )
admin.site.register( StreamType, AuditAdmin )
admin.site.register( Stream, AuditAdmin )
admin.site.register( Item, PublishableAdmin )
admin.site.register( Feed, PublishableAdmin )
admin.site.register( FeedItem, AuditAdmin )

