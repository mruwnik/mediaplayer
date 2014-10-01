from django.conf.urls import patterns, include, url
from mplayer import views

urlpatterns = patterns('',
        url(r'^command/(\w+)', views.command, name='command'),
        url(r'^play/(.+)', views.play, name='play'),
        url(r'^list_media', views.list_media, name='list_media'),
)
