from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from promocodes.forms import AddPromoCodeForm
from promocodes.models import PromoCode


# Create your views here.
def promo_codes_view(request):
    # return render(request, 'promocodes/Promo_Codes.html')
    promos = PromoCode.objects.all()
    print("We are here")
    if request.method == 'POST':
        print("--------------")
        form = AddPromoCodeForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return render(request, 'promocodes/Promo_Codes.html', {'form': form, 'promos': promos})

    else:
        form = AddPromoCodeForm
    return render(request, 'promocodes/Promo_Codes.html', {'form': form, 'promos': promos})

@login_required
def delete_promo(request, id):
    f = get_object_or_404(PromoCode, pk=id)
    f.delete()
    return redirect("promo_codes")


def get_promo(request, id):
    promo = get_object_or_404(PromoCode, pk=id)
    promo_data = {'id': promo.id, 'promo_code': promo.promo_code, 'discount': promo.discount, 'description': promo.description}
    return JsonResponse({'promo': promo_data})
