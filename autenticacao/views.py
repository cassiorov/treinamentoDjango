from django.shortcuts import render, get_list_or_404
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
import json

from .models import Pessoa, Cargos


def cadastro(request: WSGIRequest):
    if request.method == 'GET':
        params = request.GET.dict()
        return render(request, 'cadastro/index.html', {'teste': params})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        pessoa = Pessoa(
            nome=nome,
            email=email,
            senha=senha
        )
        pessoa.save()
        return HttpResponse(json.dumps({'nome': nome, 'email': email, 'senha': senha}))


def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar/listar.html', {'pessoas': pessoas})


def listar_unico(request, id_pessoa):
    pessoa = get_list_or_404(Pessoa, id=id_pessoa)
    return render(request, 'listar/listar.html', {'pessoas': pessoa})
