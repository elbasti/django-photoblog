import flickrapi

def get_flickr_photos(api_key, photoset_id):
    flickr = flickrapi.FlickrAPI(api_key)
    photoset = flickr.photosets_getPhotos(photoset_id=photoset_id,
                                          extras="date_taken,url_m")
    photos = photoset[0][:]
    return photos
