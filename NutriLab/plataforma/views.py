from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from .models import Pacientes, DadosPaciente, Refeicao, Opcao, MedidasPaciente
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import time
import os
from django.conf import settings



@login_required(login_url='/auth/logar/')
def pacientes(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        nome_filtro = request.GET.get('nome_filtro')

        if nome_filtro:
            pacientes = pacientes.filter(nome__icontains=nome_filtro)

        return render(request, 'paciente.html', {'pacientes': pacientes, 'nome_filtro': nome_filtro})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if (len(nome.strip()) == 0) or (len(sexo.strip()) == 0) or (len(idade.strip()) == 0) or (len(email.strip()) == 0) or (len(telefone.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/pacientes/')
        
        if not idade.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite uma idade válida')
            return redirect('/pacientes/')
        
        pacientes = Pacientes.objects.filter(email=email)

        if pacientes.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um paciente com esse E-mail')
            return redirect('/pacientes/')
        

        try:
            paciente = Pacientes(nome=nome,
                                sexo=sexo,
                                idade=idade,
                                email=email,
                                telefone=telefone,
                                nutri=request.user)

            paciente.save()

            messages.add_message(request, constants.SUCCESS, 'Paciênte cadastrado com sucesso')
            return redirect('/pacientes/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/pacientes/')

@login_required(login_url='/auth/logar/')
def dados_paciente_listar(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        nome_filtro = request.GET.get('nome_filtro')

        if nome_filtro:
            pacientes = pacientes.filter(nome__icontains=nome_filtro)
        
        return render(request, 'dados_paciente_listar.html', {'pacientes': pacientes, 'nome_filtro': nome_filtro})

@login_required(login_url='/auth/logar/')
def dados_paciente(request, id):
    paciente = get_object_or_404(Pacientes, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, 'Este paciente não é seu.')
        return redirect('/dados_paciente/')
    
    if request.method == "GET":
        dados_paciente = DadosPaciente.objects.filter(paciente=paciente)
        return render(request, 'dados_paciente.html', {'paciente': paciente, 'dados_paciente': dados_paciente})
    elif request.method == "POST":
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        gordura = request.POST.get('gordura')
        musculo = request.POST.get('musculo')

        hdl = request.POST.get('hdl')
        ldl = request.POST.get('ldl')
        colesterol_total = request.POST.get('ctotal')
        trigliceridios = request.POST.get('trigliceridios')

        if (len(peso.strip()) == 0) or (len(altura.strip()) == 0) or (len(gordura.strip()) == 0) or (len(musculo.strip()) == 0) or (len(hdl.strip()) == 0) or (len(ldl.strip()) == 0) or (len(colesterol_total.strip()) == 0) or (len(trigliceridios.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect(f'/dados_paciente/{id}')
        
        if not peso.isnumeric() or not altura.isnumeric() or not gordura.isnumeric() or not musculo.isnumeric() or not hdl.isnumeric() or not ldl.isnumeric() or not colesterol_total.isnumeric() or not trigliceridios.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite um valor válido')
            return redirect(f'/dados_paciente/{id}')
        
        paciente = DadosPaciente(paciente=paciente,
                             data=datetime.now(),
                             peso=peso,
                             altura=altura,
                             percentual_gordura=gordura,
                             percentual_musculo=musculo,
                             colesterol_hdl=hdl,
                             colesterol_ldl=ldl,
                             colesterol_total=colesterol_total,
                             trigliceridios=trigliceridios)

        paciente.save()

        messages.add_message(request, constants.SUCCESS, 'Dados cadastrado com sucesso')

        return redirect(f'/dados_paciente/{id}')

@login_required(login_url='/auth/logar/')
def medidas_paciente_listar(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        nome_filtro = request.GET.get('nome_filtro')

        if nome_filtro:
            pacientes = pacientes.filter(nome__icontains=nome_filtro)

        return render(request, 'medidas_paciente_listar.html', {'pacientes': pacientes, 'nome_filtro': nome_filtro})

@login_required(login_url='/auth/logar/')
def medidas_paciente(request, id):
    paciente = get_object_or_404(Pacientes, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, 'Este paciente não é seu.')
        return redirect('/medidas_paciente/')
    
    if request.method == "GET":
        medidas_paciente = MedidasPaciente.objects.filter(paciente=paciente)
        return render(request, 'medidas_paciente.html', {'paciente': paciente, 'medidas_paciente': medidas_paciente})
    elif request.method == "POST":
        torax = request.POST.get('torax')
        abdomen = request.POST.get('abdomen')
        cintura = request.POST.get('cintura')
        coxa = request.POST.get('coxa')
        braco_relaxado = request.POST.get('braco_relaxado')
        braco_contraido = request.POST.get('braco_contraido')


        if (len(torax.strip()) == 0) or (len(abdomen.strip()) == 0) or (len(cintura.strip()) == 0) or (len(coxa.strip()) == 0) or (len(braco_relaxado.strip()) == 0) or (len(braco_contraido.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect(f'/medidas_paciente/{id}')
        
        if not torax.isnumeric() or not abdomen.isnumeric() or not cintura.isnumeric() or not coxa.isnumeric() or not braco_relaxado.isnumeric() or not braco_contraido.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite um valor válido')
            return redirect(f'/medidas_paciente/{id}')
        
        medidas = MedidasPaciente(paciente=paciente,
                             data=datetime.now(),
                             torax=torax,
                             abdomen=abdomen,
                             cintura=cintura,
                             coxa=coxa,
                             braco_relaxado=braco_relaxado,
                             braco_contraido=braco_contraido)

        medidas.save()

        messages.add_message(request, constants.SUCCESS, 'Medidas cadastrado com sucesso')

        return redirect(f'/medidas_paciente/{id}')

@login_required(login_url='/auth/logar/')
@csrf_exempt
def grafico_peso(request, id):
    paciente = Pacientes.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")
    
    pesos = [dado.peso for dado in dados]
    labels = list(range(len(pesos)))
    data = {'peso': pesos,
            'labels': labels}
    return JsonResponse(data)

@login_required(login_url='/auth/logar/')
@csrf_exempt
def grafico_gordura(request, id):
    paciente = Pacientes.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")
    
    gorduras = [dado.percentual_gordura for dado in dados]
    labels = list(range(len(gorduras)))
    # labels = [dado.data for dado in dados]
    data = {'gordura': gorduras,
            'labels': labels}
    return JsonResponse(data)

@login_required(login_url='/auth/logar/')
@csrf_exempt
def grafico_musculo(request, id):
    paciente = Pacientes.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")
    
    musculo = [dado.percentual_musculo for dado in dados]
    labels = list(range(len(musculo)))
    # labels = [dado.data for dado in dados]
    data = {'musculo': musculo,
            'labels': labels}
    return JsonResponse(data)

def plano_alimentar_listar(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        nome_filtro = request.GET.get('nome_filtro')

        if nome_filtro:
            pacientes = pacientes.filter(nome__icontains=nome_filtro)

        return render(request, 'plano_alimentar_listar.html', {'pacientes': pacientes, 'nome_filtro': nome_filtro})
    
def plano_alimentar(request, id):
    paciente = get_object_or_404(Pacientes, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
        return redirect('/plano_alimentar_listar/')

    if request.method == "GET":
        r1 = Refeicao.objects.filter(paciente=paciente).order_by("horario")
        opcao = Opcao.objects.all()
        return render(request, 'plano_alimentar.html', {'paciente': paciente, 'refeicao': r1, 'opcao': opcao})
    
def refeicao(request, id_paciente):
        paciente = get_object_or_404(Pacientes, id=id_paciente)
        if not paciente.nutri == request.user:
            messages.add_message(request, constants.ERROR, 'Este paciente não é seu.')
            return redirect('/dados_paciente/')
        
        if request.method == "POST":
            titulo = request.POST.get('titulo')
            horario = request.POST.get('horario')
            carboidratos = request.POST.get('carboidratos')
            proteinas = request.POST.get('proteinas')
            gorduras = request.POST.get('gorduras')

            r1 = Refeicao(paciente=paciente,
                          titulo=titulo,
                          horario=horario,
                          carboidratos=carboidratos,
                          proteinas=proteinas,
                          gorduras=gorduras,
                          )

            r1.save()

            messages.add_message(request, constants.SUCCESS, 'Refeição cadastrada com suecsso.')
            return redirect(f'/plano_alimentar/{id_paciente}')

def opcao(request, id_paciente):
    if request.method == "POST":
        id_refeicao = request.POST.get('refeicao')
        imagem = request.FILES.get('imagem')
        descricao = request.POST.get("descricao")

        o1 = Opcao(refeicao_id=id_refeicao,
                   imagem=imagem,
                   descricao=descricao)

        o1.save()

        messages.add_message(request, constants.SUCCESS, 'Opção cadastrada com sucesso')
        return redirect(f'/plano_alimentar/{id_paciente}')
    
def mm2p(milimetros):
    return milimetros / 0.352777

def exportar_refeicao(request, id_paciente):
    paciente = get_object_or_404(Pacientes, id=id_paciente)
    refeicao = Refeicao.objects.filter(paciente=paciente).order_by("horario")
    opcao = Opcao.objects.all()
    data = datetime.now()
    data = data.strftime("%d-%m-%Y")
    
    if not paciente.nutri == request.user:
            messages.add_message(request, constants.ERROR, 'Este paciente não é seu.')
            return redirect('/dados_paciente/')
    
    eixo_y = 270

    if request.method == "GET":
        cnv = canvas.Canvas(f'media/dietas/{id_paciente}_{paciente.nome}.pdf', pagesize=A4)

        cnv.drawString(mm2p(90), mm2p(280), paciente.nome)
        cnv.setTitle(f'Plano alimentar - {paciente.nome}')

        for ref in refeicao:
            horario = ref.horario
            horario = horario.strftime("%H:%M")
            ref_comp = f"{ref.titulo} - {horario}h"
            cnv.drawString(mm2p(10), mm2p(eixo_y), ref_comp)
            eixo_y -= 10
            for opt in opcao:
                cnv.drawString(mm2p(20), mm2p(eixo_y), opt.descricao)
                eixo_y -= 10
            eixo_y -= 10
        
        
        cnv.save()

        
        messages.add_message(request, constants.SUCCESS, 'PDF gerado com sucesso.')
        return redirect(f'/plano_alimentar/{id_paciente}')

