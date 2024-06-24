from django import forms

from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'postal_code', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),

        }
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        city = cleaned_data.get('city')
        phone_number = cleaned_data.get('phone_number')

        if first_name and not first_name.istitle:
            self.add_error('first_name', 'First letter must be capitalized.')
        if first_name  and not first_name.isalpha():
            self.add_error('first_name', 'First name must contain only letters.')

        if last_name and not last_name.istitle():
            self.add_error('last_name', 'First letter must be capitalized.')
        if last_name and not last_name.isalpha():
            self.add_error('last_name', 'Last name must contain only letters.')

        if city and not city.istitle():
            self.add_error('city', 'First letter must be capitalized.')

        if city and not city.isalpha():
            self.add_error('city', 'City must contain only letters.')

        if phone_number and not phone_number.isdigit():
            self.add_error('phone_number', 'Phone number must contain only digits.')

