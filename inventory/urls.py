from django.urls import path
from django.views.generic.edit import UpdateView
from .views import AddInvoiceView, InvoiceView, InvoiceDetailView,  AddInvoiceView, UpdateInvoiceView, DeleteInvoiceView

urlpatterns = [
    path('', InvoiceView.as_view(), name='invoice'),
    path('invoice/<int:pk>',  InvoiceDetailView.as_view(), name='invoice-detail'),
    path('add_invoice/', AddInvoiceView.as_view(), name='add_invoice'),
    path('invoice/edit/<int:pk>',
         UpdateInvoiceView.as_view(), name='update_invoice'),
    path('invoice/<int:pk>/remove',
         DeleteInvoiceView.as_view(), name='delete_invoice'),
]
