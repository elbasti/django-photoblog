from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from photoblog.models import Photo

from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
import dateutil.parser
#app imports
from utils import get_flickr_photos
# Create your views here.
#Variables: should put these in a model later, for easy changing
API_KEY = '4553d5b675a520fdc88143e66ffce23f'
USER_ID = '96610073@N07'
PHOTOSET_ID = '72157634035952412'

def home(request):
    photos = Photo.objects.all().order_by('date').reverse()
    return render_to_response("photoblog/all.html",
            {'photos':photos},
             context_instance=RequestContext(request))

def paginated_home(request):
    #all_photos = Photo.objects.all().order_by('date').reverse()
    all_photos = get_flickr_photos(api_key=API_KEY, photoset_id=PHOTOSET_ID)
    for photo in all_photos:
        photo.url = photo.get('url_m')
        photo.date = dateutil.parser.parse(photo.get('datetaken'))
    all_photos.sort(key=lambda x: x.date, reverse =True)
    paginator = Paginator(all_photos, 5) #show 5 photos per page
    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    return render_to_response('photoblog/paginated.html',
            {'photos':photos},
            context_instance=RequestContext(request))
    
