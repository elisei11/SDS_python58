from django import forms

MAX_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 100)]


class AddToCartForm(forms.Form):
    quantity = forms.ChoiceField(choices=MAX_QUANTITY_CHOICES)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(AddToCartForm,self).__init__(*args, **kwargs)
        stock = kwargs.pop('stock', None)
        if stock:
            max_choices = [(i, str(i)) for i in range(1, int(stock)+1)]
        else:
            max_choices = MAX_QUANTITY_CHOICES
        self.fields['quantity'].choices = MAX_QUANTITY_CHOICES

