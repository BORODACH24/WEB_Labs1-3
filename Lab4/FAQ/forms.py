from django import forms

from FAQ.models import FAQ


class AddFAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ["question", "answer"]

    # widgets = {
    #     'image': forms.ClearableFileInput(attrs={'required': True}),
    # }
