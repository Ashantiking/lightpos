
from django.db import models
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Invoice, Order
from .forms import InvoiceForm, OrderForm, EditForm
# Create your views here.


class InvoiceView(ListView):
    model = Invoice
    template_name = 'invoice/invoice.html'
    ordering = ['-id']


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice/invoice_detail.html'


class AddInvoiceView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/add_invoice.html'


class UpdateInvoiceView(UpdateView):
    model = Invoice
    form_class = EditForm
    template_name = 'invoice/update_invoice.html'


class DeleteInvoiceView(DeleteView):
    model = Invoice
    template_name = 'invoice/delete_invoice.html'
    success_url = reverse_lazy('invoice')


class OrderView(ListView):
    model = Order
    template_name = 'invoice/invoice_detail.html'
    ordering = ['-id']


class OrderDetailView(DetailView):
    model = Order
    template_name = 'invoice/invoice_detail.html'


class AddOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'invoice/add_invoice.html'


class UpdateOrderView(UpdateView):
    model = Order
    form_class = EditForm
    template_name = 'invoice/update_invoice.html'


class DeleteOrderView(DeleteView):
    model = Order
    template_name = 'invoice/delete_invoice.html'
    success_url = reverse_lazy('Order')
