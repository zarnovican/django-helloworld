import os
import time

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Hello, world!</h2>")


def env(request):
    out=''
    for k, v in sorted(os.environ.items()):
        out += '{}={}\n'.format(k, v)

    return HttpResponse("<h2>Environment:</h2> <pre>"+out+"</pre>")


def slow_get(request, time_to_wait):
    out = ''
    for i in range(int(time_to_wait)):
        out += '.'
        time.sleep(1)
    return HttpResponse("{}. Responded after {} seconds.".format(out, time_to_wait))

