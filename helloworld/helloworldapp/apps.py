
import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class HelloworldappConfig(AppConfig):
    name = 'helloworldapp'

    def ready(self):
        logger.info('Application ready')
