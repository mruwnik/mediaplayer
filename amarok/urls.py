from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mediaplayer.views.home', name='home'),
    # url(r'^mediaplayer/', include('mediaplayer.foo.urls')),
     url(r'^pause', 'amarok.views.pause'),
     url(r'^stop', 'amarok.views.stop'),
     url(r'^volume', 'amarok.views.volume'),
     url(r'^next', 'amarok.views.next'),
     url(r'^prev', 'amarok.views.prev'),
     url(r'^info', 'amarok.views.info'),
     url(r'^position', 'amarok.views.position'),
     url(r'^playlist', 'amarok.views.playlist'),
     url(r'^play', 'amarok.views.play'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
