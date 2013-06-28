from django.contrib import admin
from photoblog.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Photo, PhotoAdmin)
