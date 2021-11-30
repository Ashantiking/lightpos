
from django.db import models
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Supplier
from .forms import SupplierForm, EditForm
# Create your views here.


class SupplierView(ListView):
    model = Supplier
    template_name = 'supplier.html'
    ordering = ['-date_created']


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'supplier_details.html'


class AddSupplierView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'add_supplier.html'


class UpdateSupplierView(UpdateView):
    model = Supplier
    form_class = EditForm
    template_name = 'update_supplier.html'


class DeleteSupplierView(DeleteView):
    model = Supplier
    template_name = 'delete_supplier.html'
    success_url = reverse_lazy('supplier')
