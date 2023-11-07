from django.shortcuts import render

from feedback.forms import AddFeedbackForm
from feedback.models import Feedback


# Create your views here.
def feedback_list(request):
    feedback = Feedback.objects.all()
    print("We are here")
    if request.method == 'POST':
        print("--------------")
        form = AddFeedbackForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return render(request, 'feedback/Feedback_List.html', {'form': form, 'feedback': feedback})

    else:
        form = AddFeedbackForm
    return render(request, 'feedback/Feedback_List.html', {'form': form, 'feedback': feedback})


def feedback_detail():
    return None


def delete_feedback():
    return None