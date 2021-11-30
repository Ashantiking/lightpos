from django.urls import path
from django.views.generic.edit import UpdateView
from .views import AddSupplierView, SupplierView, SupplierDetailView,  AddSupplierView, UpdateSupplierView, DeleteSupplierView

urlpatterns = [
    path('', SupplierView.as_view(), name='supplier'),
    path('supplier/<int:pk>', SupplierDetailView.as_view(), name='supplier-detail'),
    path('add_supplier/', AddSupplierView.as_view(), name='add_supplier'),
    path('supplier/edit/<int:pk>',
         UpdateSupplierView.as_view(), name='update_supplier'),
    path('supplier/<int:pk>/remove',
         DeleteSupplierView.as_view(), name='delete_supplier'),
]
