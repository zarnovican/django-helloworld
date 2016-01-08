import os

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    out=''
    for k, v in os.environ.items():
        out += '{}={}\n'.format(k, v)

    return HttpResponse("<h2>Hello, world!</h2> <pre>"+out+"</pre>")

