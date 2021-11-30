from supplier.models import Supplier
from product.models import Product
from django.db import models
from django.urls import reverse
from datetime import datetime, date


# Create your models here.


class Invoice(models.Model):
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    invoice_number = models.IntegerField()
    invoice_date = models.CharField(max_length=100)

    class Meta:
        ordering = ['-supplier_name']

    def __str__(self):
        return str(self.invoice_date) + ' | ' + str(self.supplier_name)

    def get_absolute_url(self):
        return reverse('invoice')


class Order(models.Model):
    quantity = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-product_name']

    def __str__(self):
        return str(self.product_name)

    def get_absolute_url(self):
        return reverse('invoice')
