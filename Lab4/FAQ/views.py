from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from FAQ.forms import AddFAQForm
from FAQ.models import FAQ


# Create your views here.
def FAQ_list(request):
    faq = FAQ.objects.all()
    print("We are here")
    if request.method == 'POST':
        print("--------------")
        form = AddFAQForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return render(request, 'FAQ/FAQ_List.html', {'form': form, 'faq': faq})

    else:
        form = AddFAQForm
    return render(request, 'FAQ/FAQ_List.html', {'form': form, 'faq': faq})


def FAQ_detail(request, id):
    faq = get_object_or_404(FAQ, pk=id)
    if not request.user.is_staff:
        return render(request, 'FAQ/FAQ_Detail.html', {'faq': faq})
    else:
        if request.method == 'POST':
            form = AddFAQForm(request.POST, instance=faq)
            if form.is_valid():
                form.save()
                return redirect('FAQ_list')
            else:
                return render(request, 'FAQ/FAQ_Details.html', {'form': form, 'faq': faq})
        else:
            form = AddFAQForm
        return render(request, 'FAQ/FAQ_Details.html', {'form': form, 'faq': faq})
    
@login_required
def delete_FAQ(request, id):
    f = get_object_or_404(FAQ, pk=id)
    f.delete()
    return redirect("FAQ_list")


def add_FAQ():
    return None


def sort_FAQ():
    return None