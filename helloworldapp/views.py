import logging
import random
from django.http import HttpResponse, HttpResponseForbidden

from metric import REQUEST_TIME, REQUEST_COUNT

logger = logging.getLogger(__name__)

def index(request):
    REQUEST_COUNT.inc()
    return HttpResponse('Hello!\n', content_type='text/plain')

# TODO: I wasn't able to write this as decorator
index = REQUEST_TIME.labels(url='index').time()(index)
