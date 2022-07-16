from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpRequest


def cadastro(request: WSGIRequest):
    teste = request.GET.dict()
    return render(request, 'cadastro/index.html', {'teste': teste})
