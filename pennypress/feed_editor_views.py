from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext

from pennypress.models import Stream, Item, Feed, FeedItem

def feed_editor(request, feed_slug="local"):
    t = loader.get_template( 'feed_editor/index.html' )

    f = Feed.objects.get(slug=feed_slug)

    c = RequestContext( request, {
        'streams':Stream.objects.all(),
        'stream_items': Item.objects.all(),
        'feed': f,
    } )
    return HttpResponse( t.render( c ) )

def bootstrap( request, path ):
    t = loader.get_template( 'bootstrap/{}'.format( path ) )
    c = RequestContext( request, {} )
    return HttpResponse( t.render( c ) )

def reset_sortkey_for_feeditem( request, feeditem_id ):
    from decimal import *
    getcontext().prec = 28
    feeditem = FeedItem.objects.get( id = feeditem_id )
    feeditem.sort_key = Decimal( request.REQUEST.get('sort-key') )
    feeditem.save()
    return HttpResponse( "Thanks" )

