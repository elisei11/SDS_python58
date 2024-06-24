from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, AuthenticationForm, UserCreationForm
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




class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username.'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password.'})



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password confirmation'})


    def clean(self):
        cleaned_data = super().clean()

        get_email = cleaned_data.get('email')
        check_emails = User.objects.filter(email=get_email)
        if check_emails:
            self.add_error('email', 'This email is already in use.')


