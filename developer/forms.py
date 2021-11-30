from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('logo', 'name', 'address', 'phone', 'email')

        widgets = {
            'logo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'company_logo'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_email'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('logo', 'name', 'address', 'phone', 'email')

        widgets = {
            'logo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'company_logo'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_email'}),

        }
