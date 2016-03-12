from django.conf.urls import url
from systemservices.contract.views import new, list, detail, remove


urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^new/$', new, name='new'),
    url(r'^detail/(?P<pk>[\w-]+)/$', detail, name='detail'),
    url(r'^remove/(?P<pk>[\w-]+)/$', remove, name='remove'),
]