from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from multiselectfield import MultiSelectField
from sets import Set
import time


'''
story
photo
video
link
user
    staffmember
comment

place-point
    dateline
    organization
        school
        business
        government
        church
    park
    field
    pollingstation
    polygon
        neighborhood
        city
        state
        county
event
tag
section
maplayer
map
product
subscription
device
app
log
person
    politician
    criminal
    businessleader
'''

class BaseAuditable( models.Model ):
    # https://docs.djangoproject.com/en/1.7/topics/db/models/#be-careful-with-related-name
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="%(app_label)s_%(class)s_creator")
    created_date = models.DateTimeField( auto_now_add=True)

    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="%(app_label)s_%(class)s_updater")
    updated_date = models.DateTimeField( auto_now=True)

    class Meta:
            abstract = True

####
#### content organization
####
# selecting a tag implies it and every tag in its ancestry up to the root
class Tag( BaseAuditable ):
    slug = models.SlugField()
    parent = models.ForeignKey( 'self', null=True, blank=True )

    def __unicode__( self ):
        if self.parent:
            return "{p} / {s}".format( p=self.parent, s=self.slug )
        return "/ {s}".format( p=self.parent, s=self.slug )
        
    def get_subtree_ids(self):
        child_ids = [self.id]
        children = Tag.objects.filter( parent=self )
        for child in children:
            child_ids.extend( child.get_subtree_ids() ) 
        return child_ids



class Nav( BaseAuditable ):
    parent = models.ForeignKey( 'self', null=True, blank=True ) 
    name = models.CharField( max_length=100)
    slug = models.SlugField()
    live  = models.NullBooleanField( null=True, blank=True, default=True )

    def __unicode__(self):
        if self.parent:
            return unicode( self.parent ) + "/" + self.slug
        return "/" + self.slug



class Section( BaseAuditable ):
    name = models.CharField( max_length=100 )
    slug = models.SlugField()

    included_tags = models.ManyToManyField(Tag, related_name="included_in")
    excluded_tags = models.ManyToManyField(Tag, related_name="excluded_from")

    external_rss_source = models.URLField( null=True, blank=True, help_text="Links come from this source." )
    external_page = models.URLField( null=True, blank=True, help_text="Links to this section will redirect to this url." )

    def __unicode__( self ):
        return "[{s}]".format( s=self.name )

    def get_stories(self):
        import operator

        include_ids = reduce( operator.add, [ t.get_subtree_ids() for t in self.included_tags.all() ] )
        exclude_ids = reduce( operator.add, [ t.get_subtree_ids() for t in self.excluded_tags.all() ] )

        stories = Story.objects\
            .filter( tags__id__in = include_ids )\
            .exclude( tags__id__in = exclude_ids )

        return stories


####
#### content
####

class BasePublishable( BaseAuditable ):
    abstract = True
    pub_date = models.DateTimeField()

    title = models.CharField( max_length=100 )
    slug = models.SlugField(unique_for_date='pub_date', max_length=100) 
    subtitle = models.CharField( max_length=200, null=True, blank=True )

    authors = models.ManyToManyField( settings.AUTH_USER_MODEL, null=True, blank=True )
    tags = models.ManyToManyField( Tag, null=True, blank=True )

    class Meta:
            abstract = True

    def __unicode__(self):
        return "{t} {p}".format( t=self.title, p=self.pub_date )

    def get_absolute_url( self, ):
        app = self._meta.app_label
        model_name = self._meta.model_name
        return "{app}/{mn}/{y}/{m}/{d}/{s}/".format(
                app=app,
                mn=model_name,
                y=self.pub_date.year,
                m=self.pub_date.month,
                d=self.pub_date.day,
                s=self.slug,
        )


class Photo( BasePublishable ):
    image = models.ImageField()

    def __unicode__(self):
        return "Photo: {r}".format( r=repr( self.image ) )


class Story( BasePublishable ):

    lead_photo = models.ForeignKey(Photo, null=True, blank=True)

    tease = models.TextField(max_length=200, null=True, blank=True)
    dateline = models.ForeignKey( 'Dateline', null=True, blank=True )
    one_off_dateline = models.CharField( max_length=100, null=True, blank=True )
    body = models.TextField(max_length=10000, null=True, blank=True)
    footer = models.TextField(max_length=200, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'stories'


class Video( BasePublishable ):
    video = models.URLField()
    photo = models.ForeignKey(Photo, null=True, blank=True)

    def __unicode__(self):
        return "Video: {r}".format( r=repr( self.video ) )

LINKTARGETS = ( 
        ('_blank', 'New Window'),
        ( '', 'Same Window' ),
)
class Link( BaseAuditable ):
    url = models.URLField()
    name = models.CharField( max_length = 100, null=True, blank=True )
    alt_text = models.CharField( max_length = 200, null=True, blank=True )
    target = models.CharField( choices=LINKTARGETS, max_length=50, null=True, blank=True )

    def __unicode__(self):
        return "[{n}][{u}]".format( n=self.name, u=self.url )


####
#### Places/Geography
####
class Point( BaseAuditable ):
    latitude = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True )
    longitude = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True )

    class Meta:
            #abstract = True
            unique_together = ( ('latitude', 'longitude'), )

    def __unicode__(self):
        return '{{"lat": "{lat}", "lon": "{lon}"}}'.format( lat=self.latitude, lon=self.longitude )

class Place( BaseAuditable ):
    name = models.CharField( max_length=80 )
    point = models.ForeignKey( Point )

    def __unicode__(self):
        return self.name


class State( BaseAuditable ):
    name = models.CharField( max_length=30 )
    abbr = models.CharField( max_length=10 )
    point = models.ForeignKey( Point, null=True, blank=True )

    def __unicode__(self):
        return self.name


class County( BaseAuditable ):
    name = models.CharField( max_length=30 )
    point = models.ForeignKey( Point, null=True, blank=True )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'counties'



class City( BaseAuditable ):
    name = models.CharField( max_length=30 )
    county = models.ForeignKey( County )
    state = models.ForeignKey( State )
    point = models.ForeignKey( Point, null=True, blank=True )

    def __unicode__(self):
        return "{c}, {s}".format( c=self.name, s=self.state.abbr )

    class Meta:
        verbose_name_plural = 'cities'


class ZipCode( BaseAuditable ):
    code = models.CharField(max_length=20, null=True )
    city = models.ForeignKey( City )
    point = models.ForeignKey( Point, null=True, blank=True )

    def __unicode__(self):
        return "{c}  {z}".format( c=self.city, z=self.code )

class Address( BaseAuditable ):
    addr1 = models.CharField( max_length=100, null=True, blank=True )
    addr2 = models.CharField( max_length=100, null=True, blank=True )
    one_off_city = models.CharField( max_length=100, null=True, blank=True )
    one_off_state = models.CharField( max_length=30, null=True, blank=True )
    zipcode = models.ForeignKey( ZipCode )

    point = models.ForeignKey( Point, null=True, blank=True )

    class Meta:
        verbose_name_plural = 'addresses'

    def __unicode__(self):
        return "{a1}; {a2}; {z}".format( a1=self.addr1, a2=self.addr2, z=self.zipcode ) 


class Dateline( BaseAuditable ): # has-a address
    name = models.CharField( max_length=100, null=True, blank=True )
    address = models.ForeignKey(Address, null=True, blank=True)

    def __unicode__(self):
        if self.name:
            return "DATELINE -- {n}".format( n=self.name )
        return unicode( self.address )


class Organization( BaseAuditable ): # should this be a has-a address
    name = models.CharField( max_length=30 )
    address = models.ForeignKey( Address, null=True, blank=True )
    # org types = govt, business, club, ??  is this real an Address or should is merely have an address

    def __unicode__(self):
        return self.name



class Sport( BaseAuditable ):
    name = models.CharField( max_length=100)
    slug = models.SlugField()

    def __unicode__(self):
        return repr(self.slug)


GRADES = (  ( -1, 'Pre-K'),
            ( 0, 'Kindergarten'),
            ( 1, 'First Grade' ),
            ( 2, 'Second Grade' ),
            ( 3, 'Third Grade' ),
            ( 4, 'Fourth Grade' ),
            ( 5, 'Fifth Grade' ),
            ( 6, 'Sixth Grade' ),
            ( 7, 'Seventh Grade' ),
            ( 8, 'Eight Grade' ),
            ( 9, 'HS Freshman' ),
            ( 10, 'HS Sophomore' ),
            ( 11, 'HS Junior' ),
            ( 12, 'HS Senior Grade' ),
            ( 13, 'Freshman' ),
            ( 14, 'Sophomore' ),
            ( 15, 'Junior' ),
            ( 16, 'Senior' ),
            ( 17, 'Associates' ),
            ( 18, 'Bachellors' ),
            ( 19, 'Masters' ),
            ( 20, 'Doctorate' ),
        )

class School( BaseAuditable ):
    name = models.CharField( max_length=100 )
    address = models.ForeignKey( Address, null=True, blank=True )
    grades = MultiSelectField( choices = GRADES )
    sports = models.ManyToManyField( Sport, null=True, blank=True )


class Park( BaseAuditable ):
    name = models.CharField( max_length=100 )
    address = models.ForeignKey( Address, null=True, blank=True )
    sports = models.ManyToManyField( Sport, null=True, blank=True )

    def __unicode__(self):
        return "{n} {z}".format( n=self.name, z=self.zipcode )


DENOMINATIONS = ( ( 'christian', 'Christian' ),
                    ( 'satanic', 'Satanic' ),
        )
class Church( BaseAuditable ):
    name = models.CharField( max_length=100 )
    address = models.ForeignKey( Address, null=True, blank=True )
    denomination = models.CharField( choices = DENOMINATIONS, max_length=20, null=True, blank=True )

    class Meta:
        verbose_name_plural = 'churches'


class PollingStation( BaseAuditable ):
    address = models.ForeignKey( Address, null=True, blank=True )
    hours = models.TextField()
    description = models.TextField()
    # are they tied to zipcodes that they serve?


####
#### Calendar
####
class EventType( BaseAuditable ):
    name = models.CharField( max_length=40 )
    live = models.NullBooleanField( default=True )

    def __unicode__(self):
        return self.name


class EventTemplate( BaseAuditable ):
    name = models.CharField( max_length=100)
    slug = models.SlugField()
    description = models.TextField( null=True, blank=True )

    eventtypes = models.ManyToManyField( EventType  )

    organization = models.ForeignKey( Organization, null=True, blank=True, related_name="eventtemplates" )
    address = models.ForeignKey(Address, null=True, blank=True, related_name="eventtemplates_for_this_address" )
    one_off_address = models.TextField( null=True, blank=True )

    start_time = models.TimeField( null=True, blank=True)
    duration = models.DecimalField( max_digits=5, decimal_places=2, help_text='Hours') # end_time = models.TimeField( null=True, blank=True)

    start_date = models.DateField( null=True, blank=True)
    end_date = models.DateField( null=True, blank=True)

    repeat_expression = models.CharField( max_length=100, null=True, blank=True, help_text='''Use the days of the Week or other expressions like:
        weekly style:
            Monday
            Monday, Wednesday, Friday
        monthly style:
            first Sunday
            last friday
            biweekly wednesdays
    ''' )

    def __unicode__(self):
        return "{o} {n} {r}".format( o=self.organization, n=self.name, r=self.repeat_expression ) 


class Event( BaseAuditable ):
    name = models.CharField( max_length=100)
    description = models.TextField( null=True, blank=True )
    eventtemplate = models.ForeignKey( EventTemplate, null=True, blank=True )

    eventtypes = models.ManyToManyField( EventType  )

    starts = models.DateTimeField()
    ends = models.DateTimeField( null=True, blank=True )

    organization = models.ForeignKey( Organization, null=True, blank=True, related_name="events" )
    address = models.ForeignKey(Address, null=True, blank=True, related_name="events_at_this_address" )
    one_off_address = models.TextField( null=True, blank=True )

    notes = models.TextField( null=True, blank=True )

    def __unicode__(self):
        return "{s} {n} {o}".format( o=self.organization, n=self.name, s=self.starts ) 

####
#### Streams/Feeds
#### - Streams are incoming content nuggets that may or may not get published or used in some particular way
#### - Feeds are outgoing, curated, formated StreamItems
####
class StreamType( BaseAuditable ): # rss stream, rss updates, page scrape, signal, plugin
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True )


    def __unicode__(self):
        return self.slug


    def process_stream( self, stream ):
        from django.utils import timezone

        if stream.update_policy == 'replace':
            Item.objects.filter( stream=stream ).delete()

        if self.slug == "rss":
            import feedparser
            f = feedparser.parse( stream.config )

            for e in f.entries:
                entry_guid = e.link + e.published
                if stream.pub_policy == 'auto':
                    item_status = 'show'
                else:
                    item_status = 'hide'

                item, is_new = Item.objects.get_or_create( stream=stream, guid=entry_guid, defaults = {
                    'title':e.title,
                    'pub_date': timezone.now(),
                    'body': e.summary,
                    'link': e.link,
                    'status': item_status,
                    'item_type': ItemType.objects.get_or_create( slug='html', description='html' )[0],
                } )
                if is_new:
                    print "adding", entry_guid
                else:
                    print "updating", entry_guid
                item.save()

                if stream.pub_policy == 'auto':
                    # put it into the feeds
                    for feed in stream.feed_set.all():
                        feed_item, is_new = FeedItem.objects.get_or_create( feed=feed, item=item, defaults={
                            'status': item_status,
                            'sort_key': time.time(),
                        } )
                        if is_new:
                            feed_item.save()

        elif self.slug == 'twitter':
            import tweepy
            # TODO: get these from the Stream.config?
            import os
            consumer_key = os.environ.get('FIRSTPOSTR_TWITTER_CONSUMER_KEY' )
            consumer_secret = os.environ.get('FIRSTPOSTR_TWITTER_CONSUMER_SECRET' )
            token = os.environ.get('FIRSTPOSTR_TWITTER_ACCESS_TOKEN' )
            secret = os.environ.get('FIRSTPOSTR_TWITTER_ACCESS_SECRET' )

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(token, secret)

            # Construct the API instance
            api = tweepy.API(
                    auth,
                    wait_on_rate_limit=True,
                    wait_on_rate_limit_notify=True,
                    timeout=60,
                    retry_delay=2,
            )

            for s in tweepy.Cursor( api.favorites).items(3):
                entry_guid = s.id
                if stream.pub_policy == 'auto':
                    item_status = 'show'
                else:
                    item_status = 'hide'

                item, is_new = Item.objects.get_or_create( stream=stream, guid=entry_guid, defaults = {
                    'title': "Tweet by {n} (@{s})".format( n=s.author.name,s=s.author.screen_name, ),
                    'pub_date': timezone.now(),
                    'slug': entry_guid,
                    'body': s.text,
                    #'link': 
                    'status': item_status,
                    'item_type': ItemType.objects.get_or_create( slug='tweet', description='tweet' )[0],
                } )
                if is_new:
                    print "adding", entry_guid
                else:
                    print "updating", entry_guid
                item.save()

                if stream.pub_policy == 'auto':
                    # put it into the feeds
                    for feed in stream.feed_set.all():
                        feed_item, is_new = FeedItem.objects.get_or_create( feed=feed, item=item, defaults={
                            'status': item_status,
                            'sort_key': time.time(),
                        } )
                        if is_new:
                            feed_item.save()


                tag_set = [] 
                for hashtag in [ tag['text'] for tag in s.entities['hashtags'] ]:
                    tag, is_new = Tag.objects.get_or_create( slug=hashtag, defaults={
                        'parent': Tag.objects.get_or_create( slug='UNMODERATED' )[0],
                    })
                    tag_set.append( tag )
                item.tags.add( *tag_set ) 



class Stream( BaseAuditable ):
    name = models.CharField( max_length=100 )
    slug = models.SlugField()
    status = models.CharField( choices=(('live','Live'),('suspended','Suspended')), max_length=10 )
    stream_type = models.ForeignKey( StreamType )
    config = models.TextField(null=True, blank=True )
    notes = models.TextField(null=True, blank=True )
    pub_policy = models.CharField( max_length=10, choices=(('manual','Manual'), ('auto','Automatic')), default='auto' )
    update_policy = models.CharField( max_length=10, choices=(('extend','Extend'), ('replace','Replace')), default='extend' )
    last_good_date = models.DateTimeField( null=True, blank=True )
    last_bad_date = models.DateTimeField( null=True, blank=True )

    
    def __unicode__(self):
        return "{n}({s})".format( n=self.name, s=self.stream_type ) 


    def update( self ):
        ''' update our stream items '''
        from django.utils import timezone
        try:
            print "{s} updating...".format( s= self ) 
            res = self.stream_type.process_stream( self )
            self.last_good_date = timezone.now()
        except Exception, e:
            print e
            self.last_bad_date = timezone.now()
        self.save()



class ItemType( BaseAuditable ): # for parsing the item body: html, markdown, link, json, model
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True )

    def __unicode__(self):
        return self.slug



class Item( BasePublishable ):
    stream = models.ForeignKey( Stream )
    item_type = models.ForeignKey( ItemType )
    guid = models.CharField( max_length=100, null=True, blank=True )
    icon = models.ImageField( upload_to="streamitems/%Y/%m/%d", null=True, blank=True )
    body = models.TextField(null=True, blank=True )
    link = models.URLField(null=True, blank=True )
    status = models.CharField( max_length=10, choices=(('show','Show'),('hide','Hide')), null=True, blank=True, default="show" )

    class Meta:
        ordering = [ '-pub_date', ]

    def __unicode__(self):
        return self.title



class Feed( BasePublishable ):
    streams = models.ManyToManyField( Stream, null=True, blank=True )

    def __unicode__(self):
        return self.title


    def update_streams(self):
        for stream in self.streams.all():
            stream.update()

    @property
    def visible_feeditems(self, limit=50):
        return self.feeditem_set.filter(status='show')


    @property
    def published_feeditems(self, limit=50):
        from django.utils import timezone
        return self.feeditem_set.filter(status='show', item__pub_date__lt=timezone.now() )



class FeedItem( BaseAuditable ):
    feed = models.ForeignKey( Feed )
    sort_key = models.DecimalField( max_digits=10+28, decimal_places=28 ) # really precise because the client will be dividing these down for sorting.
    item = models.ForeignKey( Item )
    status = models.CharField( max_length=10, choices=(('show','Show'),('hide','Hide')), null=True, blank=True, default="show" )
    #style = # md, json, fulltexthtml, summaryhtml, text, nolinks, bigbox, imageonly, imageandlink, etc

    class Meta:
        #unique_together= ( ('feed', 'sort_key'), )
        ordering = [ '-sort_key' ]


    def __unicode__(self):
        return "{t} {sk} {status}".format(t=self.item.title, sk=self.sort_key, status=self.status)
