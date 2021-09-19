from django import forms
from django.forms import TextInput, Textarea

from merch.models import Merch, MerchReal


class MerchForm(forms.ModelForm):
    class Meta:
        model = Merch
        fields = ['name', 'price', 'discount_price', 'description', 'header_image', 'for_vip']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'please insert name', 'class': 'form-control'}),
            'price': TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'discount_price': TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'please insert description', 'class': 'form-control'}),
            'for_vip': TextInput(attrs={'type': 'boolean'})
        }

    def __init__(self, *args, **kwargs):
        super(MerchForm, self).__init__(*args, **kwargs)


class MerchRealForm(forms.ModelForm):
    class Meta:
        model = MerchReal
        fields = ['name', 'price', 'description', 'header_image']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'please insert name', 'class': 'form-control'}),
            'price': TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'please insert description', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MerchRealForm, self).__init__(*args, **kwargs)
