from django.http import HttpResponse
import os
import subprocess

CONTROL_FILE = "./mplayer-control"
FILMS_DIR = '/home/dan/torrents/'

def play(request, filename):
    try:
        os.mkfifo(CONTROL_FILE)
    except OSError:
        pass

    subprocess.Popen(['mplayer', '-slave',
                  '-input', 'file=%s' % CONTROL_FILE, filename])
    return HttpResponse("Hello, world. You're at the poll index.")


def command(request, command):
    os.system('echo "%s" > %s' % (command, CONTROL_FILE))
    return HttpResponse({'command':command, 'status': 'ok'})

def list_media(request):
    files = [ f for f in os.listdir(FILMS_DIR) if os.path.isfile(os.path.join(FILMS_DIR,f)) ]
    return HttpResponse(files)

