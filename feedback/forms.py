from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['product', 'comment', 'rating']
        widgets = {
            'product': forms.HiddenInput()
        }