from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^info$', views.get_info, name='info'),
    url(r'^mgmt/health$', views.get_health, name='health'),
    url(r'^log/(?P<level>\w+)$', views.log_sample, name='log_sample'),
]
