from django.contrib import admin
from django.utils.timezone import now
from systemservices.contract.models import ContractedService


class ContractModelAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'value', 'start', 'end', 'missing_days')
    list_filter = ('client', 'service', 'start', 'end')

    def missing_days(self, obj):
        return  "{} {}".format((obj.end - now().date()).days, 'days')

    missing_days.short_description = 'missing days'
    missing_days.date = True

admin.site.register(ContractedService, ContractModelAdmin)
