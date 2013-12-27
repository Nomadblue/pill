from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pill.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^bookmarks/', include('bookmarks.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
