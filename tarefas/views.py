from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .forms import TarefasForm
from .models import TarefaModel
# Create your views here.

def tarefas_home(request):
    context = {
        "nome" : "Django",
        "tarefas" : TarefaModel.objects.all()
    }
    return render(request, 'tarefas/home.html', context)

def tarefas_add(request:HttpRequest):
    if request.method == "POST":
        formulario = TarefasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    context = {
        "form": TarefasForm
    }
    return render(request, 'tarefas/adicionar.html', context)

def tarefas_remove(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect("tarefas:home")

def tarefas_edit(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == "POST":
        formulario = TarefasForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    formulario = TarefasForm(instance=tarefa)
    context = {
        'form': formulario 
    }
    return render(request,"tarefas/editar.html", context)
