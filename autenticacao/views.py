from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpRequest
import json


def cadastro(request: WSGIRequest):
    teste = request.GET.dict()
    return render(request, 'cadastro/index.html', {'teste': teste})


def valida_formulario(request: WSGIRequest):
    dados = request.POST
    nome = dados.get('nome')
    email = dados.get('email')

    return HttpResponse(json.dumps({'nome': nome, 'email': email}))
