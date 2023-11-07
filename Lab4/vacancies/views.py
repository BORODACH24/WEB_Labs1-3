from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from vacancies.forms import AddVacancyForm
from vacancies.models import Vacancy


# Create your views here.

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    print("We are here")
    if request.method == 'POST':
        print("--------------")
        form = AddVacancyForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return render(request, 'Vacancies/Vacancies_List.html', {'form': form, 'vacancies': vacancies})

    else:
        form = AddVacancyForm
    return render(request, 'Vacancies/Vacancies_List.html', {'form': form, 'vacancies': vacancies})


@login_required
def delete_vacancy(request, id):
    f = get_object_or_404(Vacancy, pk=id)
    f.delete()
    return redirect("vacancies_list")


def vacancy_detail():
    return None