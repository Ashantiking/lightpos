

from django.urls import path
from django.views.generic.edit import UpdateView
from .views import PurchaseView
from . import views


urlpatterns = [
    path('', PurchaseView.as_view(), name='purchase'),
    path('multiply/', views.multiply, name='multiply'),
]
