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
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ('created_at',)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
