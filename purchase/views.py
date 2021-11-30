from django.db import models
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Purchase
from .form import PurchaseForm, EditForm
# Create your views here.


class PurchaseView(ListView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchase1.html'
    ordering = ['-purchasing_date']


class PurchaseView(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchase1.html'


def multiply(request):

    units_price = request.GET["price"]
    quantity = request.GET["quantity"]
    total_price = units_price * quantity

    return render(request, 'result.html', {'result': total_price})
