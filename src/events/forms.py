from django import forms
from django.forms import ModelForm
from .models import Location


# Create a Location Form
class LocationForm(ModelForm):
    class Meta:

        model = Location

        fields = ('name', 'address', 'zip_code',
                  'phone_number', 'web', 'email_address')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Location'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip-Code'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone_number': '',
            'web': '',
            'email_address': '',
        }
