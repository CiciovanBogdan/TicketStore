from django import forms
from django.forms import TextInput, Textarea

from merch.models import Merch


class MerchForm(forms.ModelForm):
    class Meta:
        model = Merch
        fields = ['name', 'price', 'description', 'header_image', 'for_city', 'for_real',
                  'for_united', 'for_barcelona', 'for_vip']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'please insert name', 'class': 'form-control'}),
            'price': TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'please insert description', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MerchForm, self).__init__(*args, **kwargs)
