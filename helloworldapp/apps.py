
import logging

from django.apps import AppConfig

from . import metric

logger = logging.getLogger(__name__)


class HelloworldappConfig(AppConfig):
    name = 'helloworldapp'

    def ready(self):
        metric.start_prometheus_push_thread()
        logger.info('Application ready')
