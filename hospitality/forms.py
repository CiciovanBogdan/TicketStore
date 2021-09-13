from django import forms
from django.forms import TextInput, Textarea

from hospitality.models import Hospitality


class HospitalityForm(forms.ModelForm):
    class Meta:
        model = Hospitality
        fields = ['name', 'price', 'description']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'please insert name', 'class': 'form-control'}),
            'price': TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'please insert description', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(HospitalityForm, self).__init__(*args, **kwargs)


class HospitalityRealForm(forms.ModelForm):
    class Meta:
        model = Hospitality
        fields = ['name','description']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'please insert name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'please insert description', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(HospitalityRealForm, self).__init__(*args, **kwargs)
