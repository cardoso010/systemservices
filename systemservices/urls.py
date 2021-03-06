"""systemservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from systemservices.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^client/', include('systemservices.client.urls', namespace='client')),
    url(r'^services/', include('systemservices.services.urls', namespace='services')),
    url(r'^contract/', include('systemservices.contract.urls', namespace='contract')),
    url(r'^product/', include('systemservices.product.urls', namespace='product')),
    url(r'^admin/', admin.site.urls),
]
