from django.http import HttpResponseRedirect

def go_away(request):
    ''' this view is just a throw away to keep us from wasting time on some 404's
    '''
    return HttpResponseRedirect("http://google.com/")

