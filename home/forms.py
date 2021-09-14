from django import forms
from django.forms import TextInput, Textarea, Select

from home.models import VIP


class VIPForm(forms.ModelForm):
    class Meta:
        model = VIP
        fields = ['title', 'price', 'description', 'vip_type']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'insert title', 'class': 'form-control'}),
            'price': TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'vip_type': Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(VIPForm, self).__init__(*args, **kwargs)
