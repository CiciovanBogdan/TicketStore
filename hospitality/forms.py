from django import forms
from django.forms import TextInput, Textarea

from hospitality.models import HospitalityPayed, HospitalityVIP


class HospitalityPayedForm(forms.ModelForm):
    class Meta:
        model = HospitalityPayed
        fields = ['name_city', 'price_city', 'description_city', 'name_barcelona', 'price_barcelona',
                  'description_barcelona']
        widgets = {
            'name_city': TextInput(attrs={'placeholder': 'please insert name', 'class': 'form-control'}),
            'name_barcelona': TextInput(attrs={'placeholder': 'please insert name', 'class': 'form-control'}),
            'price_city': TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'price_barcelona': TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'description_city': Textarea(attrs={'placeholder': 'please insert description', 'class': 'form-control'}),
            'description_barcelona': Textarea(
                attrs={'placeholder': 'please insert description', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(HospitalityPayedForm, self).__init__(*args, **kwargs)


class HospitalityVIPForm(forms.ModelForm):
    class Meta:
        model = HospitalityVIP
        fields = ['name_real', 'description_real', 'name_united', 'description_united']
        widgets = {
            'name_real': TextInput(attrs={'placeholder': 'please insert name', 'class': 'form-control'}),
            'name_united': TextInput(attrs={'placeholder': 'please insert name', 'class': 'form-control'}),
            'description_real': Textarea(attrs={'placeholder': 'please insert description', 'class': 'form-control'}),
            'description_united': Textarea(attrs={'placeholder': 'please insert description', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(HospitalityVIPForm, self).__init__(*args, **kwargs)
