from django.contrib import admin
from systemservices.core.models import Client, Service


class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'phone', 'email', 'created_at')
    list_filter = ('name', 'phone', 'email')


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_at')
    list_filter = ('name', 'value')


admin.site.register(Client, ClientModelAdmin)
admin.site.register(Service, ServiceModelAdmin)

