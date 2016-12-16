import logging
from django.http import HttpResponse

from . import metric

logger = logging.getLogger(__name__)

@metric.request_latency_seconds.time()
def index(request):
    logger.debug('index viewed')
    return HttpResponse("Hello, world. You're at the helloworld index.")
