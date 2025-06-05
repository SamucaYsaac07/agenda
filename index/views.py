from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import compromisso

# from django.http import HttpResponse

# Create your views here.

def index(request):
    marcado = compromisso.objects.all()
    return render(request, 'index.html', )

def marcar(request):
    if request.method == "POST":
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        data = request.POST['data']

        atual = compromisso.objects.create(titulo=titulo,descricao=descricao,data=data)
        atual.save()

        return redirect("/")

        # return redirect(request, "/")

    else:
        return render(request, "marcar.html")

def mostrar_compromisso(request, id):
    atual = compromisso.objects.query(id=id)
    # atual = compromisso.objects.query(id=id)
    # atual = compromisso.objects.get(id=id)
    atual = get_object_or_404(compromisso, id=id)

    return render(request, "mostrar_compromisso.html", {"compromisso":atual})
