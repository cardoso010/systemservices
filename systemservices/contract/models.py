from django.db import models


class ContractedService(models.Model):
    client = models.ForeignKey('core.Client')
    service = models.ForeignKey('core.Service')
    value = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    start = models.DateField()
    end = models.DateField()

    class Meta:
        verbose_name = 'Serviço Contratado'
        verbose_name_plural = 'Serviços Contratados'
        ordering = ['start']

    def __str__(self):
        return self.client.name
