
from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('name', 'invoice_number',  'comments', 'line_one_name', 'line_one_quantity',
                  'line_one_unit_price', 'line_one_selling_price', 'line_one_total_price', 'line_one_total_profit', 'line_one_expires',
                  'line_two_name', 'line_two_quantity', 'line_two_unit_price', 'line_two_selling_price', 'line_two_total_price', 'line_two_total_profit', 'line_two_expires',
                  'line_three_name', 'line_three_quantity', 'line_three_unit_price', 'line_three_selling_price', 'line_three_total_price', 'line_three_total_profit', 'line_three_expires',
                  'line_four_name', 'line_four_quantity', 'line_four_unit_price', 'line_four_selling_price', 'line_four_total_price', 'line_four_total_profit', 'line_four_expires',
                  'line_five_name', 'line_five_quantity', 'line_five_unit_price', 'line_five_selling_price', 'line_five_total_price', 'line_five_total_profit', 'line_five_expires',

                  )

        widgets = {
            # 'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Supplier'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '001110'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg. Some Product was damage'}),
            'line_one_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_one_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_one_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_one_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_one_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_one_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_one_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),
            'line_two_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_two_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_two_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_two_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_two_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_two_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_two_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),
            'line_three_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_three_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_three_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_three_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_three_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_three_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_three_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),
            'line_four_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_four_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_four_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_four_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_four_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_four_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_four_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),
            'line_five_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_five_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_five_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_five_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_five_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_five_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_five_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('line_one_name', 'invoice_number', 'line_one_quantity', 'line_one_total_price',
                  'line_one_total_profit', 'line_one_expires',)

        widgets = {
            # 'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Supplier'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '001110'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg. Some Product was damage'}),
            'line_one_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_one_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_one_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_one_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_one_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_one_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_one_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),
            'line_two_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_two_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_two_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_two_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_two_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_two_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_two_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),
            'line_three_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_three_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_three_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_three_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_three_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_three_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_three_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),
            'line_four_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_four_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_four_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_four_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_four_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_four_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_four_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),
            'line_five_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Name of the Product'}),
            'line_five_quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Total quantity of the Product'}),
            'line_five_unit_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_five_selling_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000,000.00'}),
            'line_five_total_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'line_five_total_profit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note about the Purchase'}),
            'line_five_expires': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'February 29, 1984'}),

        }
