
from django.db import models
from django.urls import reverse
from datetime import datetime, date

# Create your models here.


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    supplier_address = models.CharField(max_length=100)
    supplier_phone = models.CharField(max_length=100)
    supplier_email = models.EmailField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['supplier_name']

    def __str__(self):
        return self.supplier_name + ' | ' + str(self.supplier_address)

    def get_absolute_url(self):
        return reverse('supplier')
