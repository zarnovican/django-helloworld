
import logging

from prometheus_client import Counter, Summary

from em_tools.metrics import registry

# application metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request', ['url'], registry=registry)
REQUEST_COUNT = Counter('request_total', 'Number of requests', registry=registry)
