from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import Investimentoform
from django.contrib.auth.decorators import login_required

@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = Investimentoform(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimento')
    else:
        investimento_form = Investimentoform()
        formulario = {
            'formulario':investimento_form
        }
        return render(request,'investimentos/novo_investimento.html',formulario)

def investimento(request):
    dados = {
        'investimento': Investimento.objects.all()
    }
    objetos = dados['investimento']
    for objeto in objetos:
        objeto.valor = round(int(objeto.valor))

    return render(request,'investimentos/investimento.html', context=dados)

def detalhe(request,id_investimento):
    dados = Investimento.objects.get(pk=id_investimento)
    
    return render(request,'investimentos/detalhe.html', {'dados': dados})

@login_required
def editar(request,id_investimento):
    dados = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formutario = Investimentoform(instance=dados)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formutario})
    else:
        formulario = Investimentoform(request.POST, instance=dados)
        if formulario.is_valid():
            formulario.save()
            return redirect('investimento')

@login_required
def deletar(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimento')
    return render(request,'investimentos/confirmando_exclucao.html',{'investimento': investimento})

