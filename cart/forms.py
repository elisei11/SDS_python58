from django import forms

MAX_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 100)]


class AddToCartForm(forms.Form):
    quantity = forms.ChoiceField(choices=MAX_QUANTITY_CHOICES)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

