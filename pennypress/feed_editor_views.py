from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext

from pennypress.models import Stream, Item, Feed, FeedItem

from decimal import Decimal, getcontext
from sets import Set

def feed_editor(request, feed_slug="local"):
    t = loader.get_template( 'feed_editor/index.html' )

    f = Feed.objects.get(slug=feed_slug)

    c = RequestContext( request, {
        'streams':f.streams.all(),
        'stream_items':  reduce( Set.union, map( Set, [ x.item_set.all() for x in f.streams.all()])), #Item.objects.all(),
        'feed': f,
        'all_feeds': Feed.objects.all(),
    } )
    return HttpResponse( t.render( c ) )

def bootstrap( request, path ):
    t = loader.get_template( 'bootstrap/{}'.format( path ) )
    c = RequestContext( request, {} )
    return HttpResponse( t.render( c ) )

def reset_sortkey_for_feeditem( request, feed_slug, feeditem_id ):
    try:
        getcontext().prec = 28
        feeditem = FeedItem.objects.get( id = feeditem_id )
        feeditem.sort_key = Decimal( request.REQUEST.get('sort-key') )
        feeditem.save()
        return HttpResponse( "Thanks" )
    except Exception, e:
        print "oops", e
    return HttpResponse( "oops" )



def remove_feeditem_from_feed( request, feed_slug ):
    # TODO: delete it or hide it?  if we delete it, it may get re-created, 
    try:
        feeditem_id = request.REQUEST.get( 'feeditem_id' )
        feeditem = FeedItem.objects.get( id=feeditem_id )
        feeditem.status = 'hide'
        feeditem.save()
        return HttpResponse( "Thanks" )

    except Exception, e:
        print "oops", e
    return HttpResponse( "oops" )

def add_streamitem_to_feed( request, feed_slug ):
    try:
        streamitem_id = request.REQUEST.get( 'streamitem_id' )
        sort_key = request.REQUEST.get('sort_key')

        feed = Feed.objects.get( slug=feed_slug )
        streamitem = Item.objects.get( id=streamitem_id )

        feeditem, is_new = FeedItem.objects.get_or_create( feed=feed, item=streamitem, defaults={'sort_key':sort_key} )
        feeditem.status = 'show'
        feeditem.sort_key = sort_key
        feeditem.save()
        return HttpResponse( feeditem.id )
    except Exception, e:
        print "oops", e
    return HttpResponse( "oops " + str(e) )

