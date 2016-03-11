from django.contrib import admin
from systemservices.client.models import Client


class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'phone', 'email', 'created_at')
    list_filter = ('name', 'phone', 'email')


admin.site.register(Client, ClientModelAdmin)
