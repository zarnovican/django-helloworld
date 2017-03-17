
import logging
import time

from setuptools_scm import get_version

from django.apps import AppConfig
from django.conf import settings

from em_tools.metrics import setup_metrics

logger = logging.getLogger(__name__)


class HelloworldappConfig(AppConfig):
    name = 'helloworldapp'

    def ready(self):
        for i in range(10):
            logger.info('Slowly starting app %d/10', i+1)
            time.sleep(1)
        logger.info('Application ready')
        settings.VERSION = get_version()
        setup_metrics(settings)
