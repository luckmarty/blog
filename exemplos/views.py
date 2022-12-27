from django.shortcuts import render


# Create your views here.
def exemplo01(request):
    return render(request, 'exemplos/12_utilitarios.html')
