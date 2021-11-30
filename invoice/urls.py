from django.urls import path
from django.views.generic.edit import UpdateView
from .views import AddInvoiceView, InvoiceView, InvoiceDetailView,  AddInvoiceView, UpdateInvoiceView, DeleteInvoiceView, OrderView, OrderDetailView, AddOrderView, UpdateOrderView, DeleteOrderView

urlpatterns = [
    path('', InvoiceView.as_view(), name='invoice'),
    path('invoice/<int:pk>', InvoiceDetailView.as_view(), name='invoice_detail'),
    path('add_invoice/', AddInvoiceView.as_view(), name='add_invoice'),
    path('invoice/edit/<int:pk>', UpdateInvoiceView.as_view(), name='update_invoice'),
    path('invoice/<int:pk>/remove',
         DeleteInvoiceView.as_view(), name='delete_invoice'),
    path('invoice/<int:pk>', OrderView.as_view(), name='invoice_detail'),
    path('order_detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('add_order/', AddOrderView.as_view(), name='add_order'),
    path('invoice/order/edit/<int:pk>',
         UpdateOrderView.as_view(), name='update_order'),
    path('invoice/order/<int:pk>/remove',
         DeleteOrderView.as_view(), name='delete_order'),

]
