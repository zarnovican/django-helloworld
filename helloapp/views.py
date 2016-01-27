import os
import time

from django.conf import settings
from django.shortcuts import render

from django.http import HttpResponse

print('Importing helloapp/views.py')

def index(request):
    return render(request, 'helloapp/index.html')


def env(request):
    return render(request, 'helloapp/env.html', {'environ': sorted(os.environ.items())})


def slow_get(request, time_to_wait):
    out = ''
    for i in range(int(time_to_wait)):
        out += '.'
        time.sleep(1)
    return HttpResponse("{}. Responded after {} seconds.".format(out, time_to_wait))


def foo(request):
    a = 6
    b = 7
    return HttpResponse("{} - logic generated: {}".format(settings.MY_VAR, a+b))
