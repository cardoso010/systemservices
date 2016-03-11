from django.db import models


class ContractedService(models.Model):
    client = models.ForeignKey('client.Client')
    service = models.ForeignKey('services.Service')
    value = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    start = models.DateField()
    end = models.DateField()

    class Meta:
        verbose_name = 'Contract Service'
        verbose_name_plural = 'Contract Services'
        ordering = ['start']

    def __str__(self):
        return self.client.name
