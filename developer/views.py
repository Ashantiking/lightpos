from django.db import models
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView
from .models import Company
from .forms import CompanyForm, EditForm
# Create your views here.


def developer(request):
    return render(request, 'auth-signin.html', {})


class CompanyView(ListView):
    model = Company
    template_name = 'company/invoice.html'
