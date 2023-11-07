from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from news.forms import AddNewsletterForm
from news.models import Newsletter


# Create your views here.
def news_list(request):
    news = Newsletter.objects.all()
    print("We are here")
    if request.method == 'POST':
        print("--------------")
        form = AddNewsletterForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return render(request, 'news/News_List.html', {'form': form, 'news': news})

    else:
        form = AddNewsletterForm
    return render(request, 'news/News_List.html', {'form': form, 'news': news})


def news_detail(request, id):
    newsletter = get_object_or_404(Newsletter, pk=id)
    if not request.user.is_staff:
        return render(request, 'news/News_Details.html', {'newsletter': newsletter})
    else:
        if request.method == 'POST':
            form = AddNewsletterForm(request.POST, instance=newsletter)
            if form.is_valid():
                form.save()
                return redirect('news_list')
            else:
                return render(request, 'news/News_Details.html', {'form': form, 'newsletter': newsletter})
        else:
            form = AddNewsletterForm
        return render(request, 'news/News_Details.html', {'form': form, 'newsletter': newsletter})


def news_hotels():
    return None

@login_required
def add_news():
    return None


def sort_news():
    return None


@login_required
def delete_news(request, id):
    newsletter = get_object_or_404(Newsletter, pk=id)
    newsletter.delete()
    return redirect("news_list")
