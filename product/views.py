
from django.db import models
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm, EditForm
# Create your views here.


class ProductView(ListView):
    model = Product
    template_name = 'product/product.html'
    ordering = ['-date_added']


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_product.html'


class UpdateProductView(UpdateView):
    model = Product
    form_class = EditForm
    template_name = 'product/update_product.html'


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('product')
