from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField('CPF', max_length=11)
    address = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)
    number = models.CharField(max_length=30)
    cep = models.CharField('CEP', max_length=30)
    city = models.CharField(max_length=250)
    email = models.EmailField('E-mail')
    phone = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Cliente'
        ordering = ('created_at',)

    def __str__(self):
        return self.name
