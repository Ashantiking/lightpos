
from supplier.models import Supplier
#from category.models import Category
from django.db import models
from django.urls import reverse
from datetime import datetime, date

# Create your models here.


class Product(models.Model):
    product_code = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_quantity = models.CharField(max_length=255)
    product_cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    product_selling_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product_expires = models.CharField(max_length=100)
    product_notes = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['product_name']

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product')


class Inventory(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)
    cost_price = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField(auto_now_add=True)
    product_description = models.TextField(max_length=255)

    def __str__(self):
        return str(self.product) + ' | ' + str(self.quantity) + ' | ' + str(self.cost_price)

    def get_absolute_url(self):
        return reverse('inventory')
