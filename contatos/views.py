from .models import Contato
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {'contatos': contatos})
