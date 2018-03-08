from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

'''class LoginForm(forms.Form):

    usr = forms.CharField(label='Nombre de usuario')
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput())'''

class LoginForm(UserCreationForm):

    class Meta:
        model= User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        labels ={
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }