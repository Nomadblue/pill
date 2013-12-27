from django.conf.urls import patterns, url

urlpatterns = patterns('bookmarks.views',
    url(r'^$', 'home', name='home'),
    url(r'^github/$', 'github_connect', name='github_connect'),
    url(r'^github/sync/$', 'github_sync', name='github_sync'),
)
