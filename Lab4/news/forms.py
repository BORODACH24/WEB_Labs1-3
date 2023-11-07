from django import forms

from news.models import Newsletter


class AddNewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["title", "summary", "main_part", "image"]

    # widgets = {
    #     'image': forms.ClearableFileInput(attrs={'required': False}),
    # }
