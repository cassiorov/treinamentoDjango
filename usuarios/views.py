from asyncio import constants
from django.shortcuts import redirect, render
from django.contrib import messages
from hashlib import sha256


from .models import Usuario


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def valida_cadastro(request):
    campos = {
        'nome': request.POST.get('nome'),
        'email': request.POST.get('email'),
        'senha': request.POST.get('senha')
    }
    for chave, valor in campos.items():
        if len(valor) == 0:
            print(f'{chave} com valor inválido!')
            messages.add_message(request, messages.WARNING, f'O campo {chave} não pode ser vazio!')
            return redirect('/auth/cadastro/')
    if len(campos.get('senha')) < 4:
        messages.add_message(request, messages.WARNING, 'Sua senha não pode conter menos de 4 caracteres')
        return redirect('/auth/cadastro/')

    usuario = Usuario.objects.filter(email=campos.get('email'))
    if usuario:
        messages.add_message(request, messages.WARNING, 'Usuário já cadastrado, realize o login')
        return redirect('/auth/cadastro/')
    try:
        user = Usuario(
            nome=campos.get('nome'),
            email=campos.get('email'),
            senha=sha256(campos.get('senha').encode()).hexdigest()
        )
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('/auth/cadastro/')
    except Exception as e:
        print(e)
        messages.add_message(request, messages.ERROR, 'Erro interno do sistema ao realizar o login')
        return redirect('/auth/cadastro/')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha)
    if not usuario:
        messages.add_message(request, messages.WARNING, 'Email ou senha inválidos')
        return redirect('/auth/login/')
    else:
        request.session['logado'] = True
        return redirect('/plataforma/home/')


def sair(request):
    request.session.flush()
    messages.add_message(request, messages.SUCCESS, 'Você foi desconectado com sucesso!')
    return redirect('/auth/login/')
