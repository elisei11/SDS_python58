from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Description'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Stock'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter Product Category'}),
            'image': forms.FileField()
        }