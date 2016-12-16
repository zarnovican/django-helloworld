import logging
import random
from django.http import HttpResponse, HttpResponseForbidden

from . import metric

logger = logging.getLogger(__name__)

@metric.request_latency_seconds.time()
def index(request):
    logger.debug('index viewed')
    if random.randint(0, 100) < 10:
        metric.response_code_total.labels(code=403).inc()
        return HttpResponseForbidden()
    metric.response_code_total.labels(code=200).inc()
    return HttpResponse("Hello, world. You're at the helloworld index.")
