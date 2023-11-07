from django import forms

from feedback.models import Feedback
from news.models import Newsletter
from promocodes.models import PromoCode


class AddPromoCodeForm(forms.ModelForm):
    class Meta:
        model = PromoCode
        fields = ["promo_code", "discount", "finish_date", "description"]
