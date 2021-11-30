from django.urls import path
from django.views.generic.edit import UpdateView
from .views import AddProductView, ProductView, ProductDetailView,  AddProductView, UpdateProductView, DeleteProductView

urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('product/<int:pk>',  ProductDetailView.as_view(), name='product-detail'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('product/edit/<int:pk>',
         UpdateProductView.as_view(), name='update_product'),
    path('product/<int:pk>/remove',
         DeleteProductView.as_view(), name='delete_product'),
]
