
import logging

from django.apps import AppConfig
from django.conf import settings

from em_tools.metrics import setup_metrics

logger = logging.getLogger(__name__)


class HelloworldappConfig(AppConfig):
    name = 'helloworldapp'

    def ready(self):
        logger.info('Application ready')
        setup_metrics(settings)
