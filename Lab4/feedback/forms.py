from django import forms

from feedback.models import Feedback
from news.models import Newsletter


class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["last_name", "first_name", "patronymic", "stars", "main_part"]
