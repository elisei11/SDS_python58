from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
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

class PasswordChange(PasswordChangeForm):

    class Meta:
        model= User
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})


