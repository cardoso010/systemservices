from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

