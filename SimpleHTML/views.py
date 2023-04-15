from django.shortcuts import render

from .models import Contato


def index(request):
    return render(request, 'index.html')


def salvar_contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        contato = Contato(nome=nome, telefone=telefone, email=email, mensagem=mensagem)
        contato.save()
        print("salvo")
        return render(request, 'sucesso.html')

    return render(request, 'index.html')


def sucesso(request):
    return render(request, 'sucesso.html')
