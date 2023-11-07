from django import forms

from vacancies.models import Vacancy


class AddVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ["title", "job_type", "description"]

