
import os

from django.shortcuts import render


def index(request):
    return render(request, 'helloworld/index.html')

def env(request):
    return render(request, 'helloworld/env.html', {'environ': sorted(os.environ.items())})
