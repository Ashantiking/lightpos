from django.urls import path
from django.views.generic.edit import UpdateView
from .views import OrderView, OrderDetailView, AddOrderView, UpdateOrderView, DeleteOrderView


urlpatterns[
    path('', OrderView.as_view(), name='invoice_detail'),
    path('order_detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('add_order/', AddOrderView.as_view(), name='add_order'),
    path('invoice/order/edit/<int:pk>',
         UpdateOrderView.as_view(), name='update_order'),
    path('invoice/order/<int:pk>/remove',
         DeleteOrderView.as_view(), name='delete_order'),

]
