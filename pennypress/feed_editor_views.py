from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext

from pennypress.models import Stream, Item
def feed_editor(request):
    t = loader.get_template( 'feed_editor/index.html' )
    c = RequestContext( request, {
        'streams':Stream.objects.all(),
        'stream_items': Item.objects.all(),
    } )
    return HttpResponse( t.render( c ) )

def bootstrap( request, path ):
    t = loader.get_template( 'bootstrap/{}'.format( path ) )
    c = RequestContext( request, {} )
    return HttpResponse( t.render( c ) )

