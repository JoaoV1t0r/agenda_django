from django.core import paginator
from .models import Contato
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {'contatos': contatos})


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if contato.mostrar:
        return render(request, 'contatos/ver_contato.html', {'contato': contato})
    else:
        raise Http404()


def busca(request):
    termo = request.GET.get('termo')

    if termo is None:
        raise Http404()

    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        mostrar=True
    )
    paginator = Paginator(contatos, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {'contatos': contatos})
