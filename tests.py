"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from photoblog.models import Photo
#Pages Work Tests

class ClientTests(TestCase):
    def setUp(self):
        self.c = Client()
        test_photo = Photo(date='1987-02-16', 
                           url='http://www.elbasti.com') 
        test_photo.save()

    def test_photos_work(self):
        response = self.c.get('/photo/')
        self.assertEqual(response.status_code, 200, "Photo page is not 200")
        #below won't work if test db is empty
        self.assertNotEqual(len(response.context['photos']),0, "No photos in page")

