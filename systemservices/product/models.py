from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    value = models.DecimalField(decimal_places=3, max_digits=20)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ManyToManyField('product.Product')
    client = models.ForeignKey('client.Client', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sale'
        ordering = ('-created_at', )

    def __str__(self):
        return self.product