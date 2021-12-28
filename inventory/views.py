
from django.db import models
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Invoice
from .forms import InvoiceForm, EditForm
# Create your views here.


class InvoiceView(ListView):
    model = Invoice
    template_name = 'inventory/invoice.html'
    ordering = ['-date_added']


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'inventory/invoice_details.html'


class AddInvoiceView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'inventory/add_invoice.html'


class UpdateInvoiceView(UpdateView):
    model = Invoice
    form_class = EditForm
    template_name = 'inventory/update_invoice.html'


class DeleteInvoiceView(DeleteView):
    model = Invoice
    template_name = 'inventory/delete_invoice.html'
    success_url = reverse_lazy('invoice')
