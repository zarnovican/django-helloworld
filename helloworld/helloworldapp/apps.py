
import logging

from django.apps import AppConfig

from . import metric

try:
    from uwsgidecorators import postfork
except ImportError:
    postfork = lambda x: x

logger = logging.getLogger(__name__)

@postfork
def start_prometheus_push_thread():
    metric.start_prometheus_push_thread()


class HelloworldappConfig(AppConfig):
    name = 'helloworldapp'

    def ready(self):
        logger.info('Application ready')
