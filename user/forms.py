from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput

from user.models import ExtendUser


class UserForm(UserCreationForm):
    class Meta:
        model = ExtendUser
        fields = ['first_name', 'last_name', 'username', 'email', 'age', 'balance']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'insert first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'insert last name', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'insert username', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'insert email', 'class': 'form-control', 'type': 'email'}),
            'age': TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'balance': TextInput(attrs={'class': 'form-control', 'type': 'number'})
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'insert password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
