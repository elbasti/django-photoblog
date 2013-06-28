from django.conf.urls import patterns, include, url

urlpatterns = patterns('photoblog.views',
        url(r'^$', 'paginated_home'),
        url(r'^all$', 'home'),
        )

