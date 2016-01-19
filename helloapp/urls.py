
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^env$', views.env, name='env'),
    url(r'^slow/(?P<time_to_wait>[0-9]+)$', views.slow_get, name='slow_get'),
]
