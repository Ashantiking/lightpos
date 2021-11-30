
from django.db import models
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from order.models import Order
from .forms import OrderForm, EditForm
# Create your views here.


class OrderView(ListView):
    model = Order
    template_name = 'invoice/invoice_detail.html'
    ordering = ['-id']


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'


class AddOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/add_order.html'
    success_url = reverse_lazy('invoice', kwargs={'pk': self.pk
                                                  })


# Create your views here.
