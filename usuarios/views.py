from django.shortcuts import redirect, render
from django.http import HttpResponse
from hashlib import sha256

from .models import Usuario


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    campos = {
        'nome': request.POST.get('nome'),
        'email': request.POST.get('email'),
        'senha': request.POST.get('senha')
    }
    for chave, valor in campos.items():
        if len(valor) == 0:
            print(f'{chave} com valor inválido!')
            return redirect('/auth/cadastro/?status=1')
    if len(campos.get('senha')) < 4:
        return redirect('/auth/cadastro/?status=2')

    usuario = Usuario.objects.filter(email=campos.get('email'))
    if usuario:
        return redirect('/auth/cadastro/?status=3')

    try:
        user = Usuario(
            nome=campos.get('nome'),
            email=campos.get('email'),
            senha=sha256(campos.get('senha').encode()).hexdigest()
        )
        user.save()
        return redirect('/auth/cadastro/?status=0')
    except Exception as e:
        print(e)
        return redirect('/auth/cadastro/?status=4')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha)
    if usuario:
        return redirect('/auth/login/?status=1')
    else:
        pass
