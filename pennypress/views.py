from django.shortcuts import render
from django.shortcuts import get_object_or_404

from pennypress.models import Story, Section, Event
from pennypress.models import Feed

def home(request, template="home.html" ):
 

    # build home cotext
    ctxt = {
       'greet': 'Welcome',
    }
    
    #render response
    response = render( request, template, ctxt ) 

    # apply cookies
    return response


def section( request, slug, template="section.html" ):
    section = get_object_or_404( Section, slug=slug )

    ctxt = {
        'section': section,
    }
    return render( request, template, ctxt )


def story_detail( request, path, slug, template="story_detail.html" ):
    pass


def feed_view( request, feed_slug, template="feed.html" ):
    feed = Feed.objects.get( slug=feed_slug )
    ctxt = {
        'feed': feed,
    }
    print feed
    return render( request, template, ctxt )
