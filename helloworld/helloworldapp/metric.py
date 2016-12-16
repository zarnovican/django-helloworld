
import logging
import os
import psutil
import time
import threading
from urllib.error import  URLError

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, Summary

logger = logging.getLogger(__name__)

registry = CollectorRegistry()

def prometheus_push():
    logger.debug('init')
    p = psutil.Process(os.getpid())
    process_name = p.cmdline()[0]
    if not process_name.startswith('uWSGI worker '):
        logger.warning('Prometheus client not started. Worker\'s process name ("{}") should'
                       ' contain "uWSGI worker" string, please start uwsgi'
                       ' with --auto-procname option.'.format(process_name))
        return

    worker_id = process_name.split()[2]
    logger.debug('entering loop')
    while True:
        logger.debug('pushing..')
        try:
            push_to_gateway('localhost:9091', job='helloworld', registry=registry,
                            grouping_key={'service': 'helloworld', 'worker': worker_id, })
        except URLError as e:
            logger.warning('Failed to push Prometheus metrics ({})'.format(e))
        time.sleep(10)

def start_prometheus_push_thread():
    logger.debug('creating "prometheus_push" thread')
    t = threading.Thread(target=prometheus_push)
    t.setDaemon(True)
    t.start()
