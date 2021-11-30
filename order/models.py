from supplier.models import Supplier
from invoice.models import Invoice
from product.models import Product
from django.db import models
from django.urls import reverse
from datetime import datetime, date

# Create your models here.


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
        return reverse('invoice', kwargs={'invoice.pk': self.pk
                                          })
