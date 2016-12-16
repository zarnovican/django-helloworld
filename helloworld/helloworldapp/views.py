import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.debug('index viewed')
    return HttpResponse("Hello, world. You're at the helloworld index.")
