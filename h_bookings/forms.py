from django import forms
from django.forms import TextInput, Select, Textarea

from h_bookings.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'date', 'nr_of_persons', 'other_details']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'insert first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'insert last name', 'class': 'form-control'}),
            'date': Select(attrs={'class': 'form-control'}),
            'nr_of_persons': TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'other_details': Textarea(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
