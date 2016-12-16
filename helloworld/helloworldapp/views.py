import logging
import random
from django.http import HttpResponse, HttpResponseForbidden

from . import metric

logger = logging.getLogger(__name__)

@metric.request_latency_seconds.time()
def index(request):
    logger.debug('index viewed')
    if random.randint(0, 100) < 10:
        return HttpResponseForbidden()
    return HttpResponse("Hello, world. You're at the helloworld index.")
