from django.shortcuts import render
from django.http import HttpResponse
from . import getComentarioMLB

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def pesquisa_produto(request):
    if request.method == "GET":
        return render(request, 'index.html')
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        listaprod = getComentarioMLB.getMLB(nome)
        if listaprod == 'sem acesso ao anuncio':
            return render(request, 'index.html')
        else:
            return render(request,'teladepesquisa.html',{'produto':listaprod})

def visualizar_produto(request):
    url = request.POST.get('urlProd')
    img = request.POST.get('imgprod')
    preco = request.POST.get('prodPreco')
    comentario=getComentarioMLB.mlbanuncio(url,'p','ui-review-capability-comments__comment__content ui-review-capability-comments__comment__content')
    titulo = getComentarioMLB.mlbanuncio(url,'h1','ui-pdp-title')
    avaliacao = getComentarioMLB.mlbanuncio(url,'span','ui-pdp-review__rating')
    return render(request, 'produto.html',{'comentario':comentario, 'titulo':titulo, 'img':img, 'avaliacao':avaliacao, 'preco':preco,'url':url})
