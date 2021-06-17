from django.core import paginator
from .models import Contato
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404


def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 1)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {'contatos': contatos})


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if contato.mostrar:
        return render(request, 'contatos/ver_contato.html', {'contato': contato})
    else:
        raise Http404()
    # try:
    #     contato = Contato.objects.get(id=contato_id)
    #     return render(request, 'contatos/ver_contato.html', {'contato': contato})
    # except Contato.DoesNotExist as e:
    #     raise Http404()
