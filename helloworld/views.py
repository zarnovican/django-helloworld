
import os
import time

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

print('importing helloworld/views.py')

VERSION = 'v1.0'

def index(request):
    return render(request, 'helloworld/index.html')


def env(request):
    return render(request, 'helloworld/env.html', {'environ': sorted(os.environ.items())})


def meta(request):
    return render(request, 'helloworld/meta.html', {'meta': sorted(request.META.items())})


def slow_get(request, time_to_wait):
    out = ''
    for i in range(int(time_to_wait)):
        out += '.'
        time.sleep(1)
    return HttpResponse("{}. Responded after {} seconds.".format(out, time_to_wait))


def version(request):
    return HttpResponse("settings: {} - code: {}".format(settings.HELLOWORLD_VERSION, VERSION))
