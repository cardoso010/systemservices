from django.conf.urls import url
from systemservices.product.views import list, new, detail, remove

urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^new/$', new, name='new'),
    url(r'^detail/(?P<pk>[\w-]+)/$', detail, name='detail'),
    url(r'^remove/(?P<pk>[\w-]+)/$', remove, name='remove'),
]
