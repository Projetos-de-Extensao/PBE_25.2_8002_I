from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html')


def cadastros(request):
    return render(request, 'cadastros.html')


def proposta(request):
    return render(request, 'proposta.html')

