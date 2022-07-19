from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    if request.session.get('logado'):
        return render(request, 'home.html')

    messages.add_message(request, messages.WARNING, 'Realize o login para acessar a plataforma')
    return redirect('/auth/login/')
