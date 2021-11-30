
from django.db import models
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView
from .models import Category
from .form import ProductForm, EditForm
# Create your views here.

class CategoryView(ListView):
    model         = Category
    template_name = 'category.html'
    ordering      = ['-ordering_date']

