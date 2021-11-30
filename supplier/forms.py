
from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('supplier_name', 'supplier_address',
                  'supplier_phone', 'supplier_email')

        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'supplier_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'supplier_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone eg +23177887035'}),
            'supplier_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'supplier@gmail.com'}),



        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('supplier_name', 'supplier_address',
                  'supplier_phone', 'supplier_email')

        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'supplier_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'supplier_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone eg +23177887035'}),
            'supplier_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'supplier@gmail.com'}),




        }
