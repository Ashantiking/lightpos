from django.urls import path
from django.views.generic.edit import UpdateView
from .views import OrderView, OrderDetailView, AddOrderView, UpdateOrderView, DeleteOrderView


urlpatterns[
    path('', Product1View.as_view(), name='invoice_detail'),

]
