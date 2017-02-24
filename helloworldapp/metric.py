
import logging
import os
import time
import threading

try:
    # Py3
    from urllib.error import URLError
except ImportError:
    # Py2
    from urllib2 import URLError

from prometheus_client import CollectorRegistry, Counter, Gauge, push_to_gateway, Summary

logger = logging.getLogger(__name__)

registry = CollectorRegistry()

# application metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request', ['url'], registry=registry)
REQUEST_COUNT = Counter('request_total', 'Number of requests', registry=registry)

def prometheus_push():
    logger.debug('init')
    logger.debug('entering loop')
    while True:
        logger.debug('pushing..')
        try:
            push_to_gateway('localhost:9091', job='helloworld', registry=registry)
        except URLError as e:
            logger.warning('Failed to push Prometheus metrics ({})'.format(e))
        time.sleep(10)

def start_prometheus_push_thread():
    logger.debug('creating "prometheus_push" thread')
    t = threading.Thread(target=prometheus_push)
    t.setDaemon(True)
    t.start()
