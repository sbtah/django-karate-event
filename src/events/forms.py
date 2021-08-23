from django import forms
from django.forms import ModelForm
from .models import Location, Event


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


class EventForm(ModelForm):

    class Meta:

        model = Event

        fields = ('name', 'event_date', 'location',
                  'manager', 'description', 'attendees')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Event'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            'location': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Location'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Manager'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
        }

        labels = {
            'name': 'Name',
            'event_date': 'Date',
            'location': 'Location',
            'manager': 'Manager',
            'description': 'Description',
            'attendees': 'Attendees',
        }
