from django.conf.urls import url
from systemservices.client.views import list, new, detail


urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^new/$', new, name='new'),
    url(r'^detail/(?P<pk>[\w-]+)/$', detail, name='detail'),
]