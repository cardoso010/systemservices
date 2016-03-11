from django.contrib import admin
from systemservices.services.models import Service


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_at')
    list_filter = ('name', 'value')


admin.site.register(Service, ServiceModelAdmin)

