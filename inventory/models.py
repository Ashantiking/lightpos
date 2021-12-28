from django.db import models
from supplier.models import Supplier
from product.models import Product
# Create your models here.


class Invoice(models.Model):
    name = models.ForeignKey(
        Supplier, related_name='SupplierName',  on_delete=models.CASCADE)
    invoice_number = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(
        auto_now_add=True, auto_now=False, blank=True, null=True)
    comments = models.TextField(
        max_length=3000, default='', blank=True, null=True)
    line_one_name = models.ForeignKey(
        Product, related_name='Product1', on_delete=models.CASCADE, default='', blank=True, null=True)
    line_one_quantity = models.IntegerField(
        default=0, blank=True, null=True)
    line_one_unit_price = models.IntegerField(default=0, blank=True, null=True)
    line_one_selling_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_one_total_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_one_total_profit = models.IntegerField(
        default=0, blank=True, null=True)
    line_one_expires = models.DateField(auto_now_add=False, auto_now=False)
    line_two_name = models.ForeignKey(
        Product, related_name='Product2', on_delete=models.CASCADE, default='', blank=True, null=True)
    line_two_quantity = models.IntegerField(
        default=0, blank=True, null=True)
    line_two_unit_price = models.IntegerField(default=0, blank=True, null=True)
    line_two_selling_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_two_total_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_two_total_profit = models.IntegerField(
        default=0, blank=True, null=True)
    line_two_expires = models.DateField(auto_now_add=False, auto_now=False)
    line_three_name = models.ForeignKey(
        Product, related_name='Product3', on_delete=models.CASCADE, default='', blank=True, null=True)
    line_three_quantity = models.IntegerField(
        default=0, blank=True, null=True)
    line_three_unit_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_three_selling_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_three_total_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_three_total_profit = models.IntegerField(
        default=0, blank=True, null=True)
    line_three_expires = models.DateField(auto_now_add=False, auto_now=False)
    line_four_name = models.ForeignKey(
        Product, related_name='Product4', on_delete=models.CASCADE, default='', blank=True, null=True)
    line_four_quantity = models.IntegerField(
        default=0, blank=True, null=True)
    line_four_unit_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_four_selling_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_four_total_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_four_total_profit = models.IntegerField(
        default=0, blank=True, null=True)
    line_four_expires = models.DateField(auto_now_add=False, auto_now=False)
    line_five_name = models.ForeignKey(
        Product, related_name='Product5', on_delete=models.CASCADE, default='', blank=True, null=True)
    line_five_quantity = models.IntegerField(
        default=0, blank=True, null=True)
    line_five_unit_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_five_selling_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_five_total_price = models.IntegerField(
        default=0, blank=True, null=True)
    line_five_total_profit = models.IntegerField(
        default=0, blank=True, null=True)
    line_five_expires = models.DateField(auto_now_add=False, auto_now=False)
    phone_number = models.ForeignKey(
        Product, on_delete=models.CASCADE, default='', blank=True, null=True)
    total = models.IntegerField(default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(
        auto_now_add=False, auto_now=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
        ('Receipt', 'Receipt'),
        ('Proforma Invoice', 'Proforma Invoice'),
        ('Invoice', 'Invoice'),
    )
    invoice_type = models.CharField(
        max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.invoice_number
