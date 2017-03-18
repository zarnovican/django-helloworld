import logging
import random
import socket

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden

from metric import REQUEST_TIME, REQUEST_COUNT

logger = logging.getLogger(__name__)

def index(request):
    REQUEST_COUNT.inc()
    return HttpResponse('Hello!\n', content_type='text/plain')

# TODO: I wasn't able to write this as decorator
index = REQUEST_TIME.labels(url='index').time()(index)

def get_info(request):
    REQUEST_COUNT.inc()

    iam = settings.SERVICE_NAME
    if settings.DOCKER_TASK_SLOT:
        iam += '.{}'.format(settings.DOCKER_TASK_SLOT)

    return HttpResponse('Django {} ({}) on {}: your IP {}\n'.format(
        iam, settings.VERSION, socket.gethostname(), request.META['REMOTE_ADDR']),
        content_type='text/plain')

get_info = REQUEST_TIME.labels(url='info').time()(get_info)

def get_health(request):
    REQUEST_COUNT.inc()
    return HttpResponse('ok\n', content_type='text/plain')

get_health = REQUEST_TIME.labels(url='health').time()(get_health)

def log_sample(request, level):
    REQUEST_COUNT.inc()
    level = level.lower()
    some_extra_info = 'fooo'
    logging.debug('"log_sample" called')
    if level == 'info':
        logging.info('This is a sample info message')
    elif level == 'warning':
        logging.warning('This is a sample warning message\n    multi\n  multi-line with extra=%s', some_extra_info)
    elif level == 'error':
        logging.error("""Agghrrr! Something horrible ..
    ..just happened. We are all doomed (extra=%s)""", some_extra_info)
    elif level == 'exception':
        1/0
    else:
        return HttpResponse('"{}" not recognized\n'.format(level), content_type='text/plain')

    return HttpResponse('ok\n', content_type='text/plain')

log_sample = REQUEST_TIME.labels(url='log_sample').time()(log_sample)
