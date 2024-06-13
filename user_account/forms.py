from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']



        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Last Name'}),

        }

