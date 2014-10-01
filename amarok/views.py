import dbus

from django.http import HttpResponse
from django.utils import simplejson

def info(request):
    session_bus = dbus.SessionBus()
    player = session_bus.get_object('org.kde.amarok', '/Player')
    iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')

    metadata = iface.GetMetadata()
    return HttpResponse(simplejson.dumps(metadata))

def pause(request):
    session_bus = dbus.SessionBus()
    player = session_bus.get_object('org.kde.amarok', '/Player')
    iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')

    metadata = iface.GetMetadata()
    iface.Pause()

    return HttpResponse(simplejson.dumps(metadata))

def stop(request):
    session_bus = dbus.SessionBus()
    player = session_bus.get_object('org.kde.amarok', '/Player')
    iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')
    iface.Stop()
    metadata = iface.GetMetadata()
    return HttpResponse(simplejson.dumps(metadata))

def volume(request):
    session_bus = dbus.SessionBus()
    player = session_bus.get_object('org.kde.amarok', '/Player')
    iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')

    if request.GET.get('volume', None):
        iface.VolumeSet(int(request.GET.get('volume', None)))
    elif request.GET.get('down', None):
        iface.VolumeDown(int(request.GET.get('down', None)))
    elif request.GET.get('up', None):
        iface.VolumeUp(int(request.GET.get('up', None)))
    return HttpResponse(simplejson.dumps({'volume' : iface.VolumeGet()}))

def prev(request):
    session_bus = dbus.SessionBus()
    player = session_bus.get_object('org.kde.amarok', '/Player')
    iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')
    iface.Prev()
    metadata = iface.GetMetadata()
    return HttpResponse(simplejson.dumps(metadata))

def next(request):
    session_bus = dbus.SessionBus()
    player = session_bus.get_object('org.kde.amarok', '/Player')
    iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')
    iface.Next()
    metadata = iface.GetMetadata()
    return HttpResponse(simplejson.dumps(metadata))

def position(request):
    session_bus = dbus.SessionBus()
    player = session_bus.get_object('org.kde.amarok', '/Player')
    iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')

    if request.GET.get('forward', None):
        iface.Forward(int(request.GET.get('forward', None)))
    elif request.GET.get('back', None):
        iface.Backward(int(request.GET.get('back', None)))
    elif request.GET.get('set', None):
        iface.PositionSet(int(request.GET.get('set', None)))

    metadata = iface.GetMetadata()
    return HttpResponse(simplejson.dumps({'current' : iface.PositionGet(),
                                          'end' : metadata['mtime']}))

def playlist(request):
    session_bus = dbus.SessionBus()
    player = session_bus.get_object('org.kde.amarok', '/TrackList')
    iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')

    random = request.GET.get('random', None)
    if random == 'true':
        iface.SetRandom(True)
    elif random == 'false':
        iface.SetRandom(False)

    if request.GET.get('get', None):
        if request.GET.get('get', None) == "current":
            metadata = iface.GetMetadata(iface.GetCurrentTrack())
            return HttpResponse(simplejson.dumps([iface.GetCurrentTrack(),metadata]))
  
        
    start = int(request.GET.get('from', "-1"))
    if start > iface.GetLength():
        start = iface.GetLength()
    end = ""
    if start >= 0:
        end = int(request.GET.get('to', None))
        if not end or end <= start: 
            end = start + 1
        elif end > iface.GetLength():
            end = iface.GetLength()
        songs = []
        for i in range(start, end):
            songs.append((i,iface.GetMetadata(i)))
        return HttpResponse(simplejson.dumps(songs))
    
    songs = []
    for i in range(iface.GetLength()):
        songs.append((i,iface.GetMetadata(i)))
    return HttpResponse(simplejson.dumps(songs))

def play(request):
    session_bus = dbus.SessionBus()
    player = session_bus.get_object('org.kde.amarok', '/TrackList')
    iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')

    if request.GET.get('track', None):
        iface.PlayTrack(int(request.GET.get('track', None)))

    metadata = iface.GetMetadata(iface.GetCurrentTrack())
    return HttpResponse(simplejson.dumps(metadata))


