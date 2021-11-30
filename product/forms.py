
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_code', 'product_name', 'product_quantity', 'product_cost_price',
                  'product_selling_price', 'supplier', 'product_expires',)

        widgets = {
            # 'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'product_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0908'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'product_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'product_cost_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'product_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'supplier': forms.Select(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'product_notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'product_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_code', 'product_name', 'product_quantity', 'product_cost_price',
                  'product_selling_price', 'supplier', 'product_expires',)

        widgets = {
            # 'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'product_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0908'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'product_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'product_cost_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'product_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'supplier': forms.Select(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'product_notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'product_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),

        }
