from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Photo(models.Model):
    date = models.DateField()
    url = models.URLField()
    caption = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(u'%s%s' % (self.date, self.location))
        super(Photo, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s %s' % (self.date, self.location)
