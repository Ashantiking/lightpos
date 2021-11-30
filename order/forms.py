
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product_name', 'quantity', 'unit_price', 'selling_price')

        widgets = {
            'product_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product_name', 'quantity', 'unit_price', 'selling_price')

        widgets = {
            'product_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),

        }
