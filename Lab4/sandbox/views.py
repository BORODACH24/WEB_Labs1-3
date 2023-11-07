from django.shortcuts import render


# Create your views here.
def sandbox_view(request):
    return render(request, 'sandbox/Sandbox.html')
