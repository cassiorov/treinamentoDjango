from django.shortcuts import render
from django.http import HttpResponse


def cadastro(request):
    pessoas = [{
        'nome': 'Cassio Alves',
        'idade': 35,
        'profissao': 'Desenvolvedor'
    },
        {
        'nome': 'Caio',
        'idade': 22,
        'profissao': 'Professor'
    }]

    return render(request, 'cadastro/index.html', {'pessoas': pessoas})
