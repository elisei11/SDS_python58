from django import forms


class AddToFavoriteForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())




