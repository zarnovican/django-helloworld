
import os
import time

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'helloworld/index.html')


def env(request):
    return render(request, 'helloworld/env.html', {'environ': sorted(os.environ.items())})


def slow_get(request, time_to_wait):
    out = ''
    for i in range(int(time_to_wait)):
        out += '.'
        time.sleep(1)
    return HttpResponse("{}. Responded after {} seconds.".format(out, time_to_wait))
