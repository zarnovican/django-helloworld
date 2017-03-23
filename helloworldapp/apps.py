
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
        logger.info('Application starting..')
        # simulate slow startup
        for i in range(settings.DJANGO_STARTUP_TIME):
            logger.info('Slowly starting app %d/%d', i+1, settings.DJANGO_STARTUP_TIME)
            time.sleep(1)
        settings.VERSION = get_version()
        setup_metrics(settings)
        logger.info('Application ready')
