from django.shortcuts import render

from site_controle.models import Motorista, Paciente, Viagem

def index(request):

    #Acessando o todos os objetos, contando e adicionando a uma variavel
    qtd_pacientes = Paciente.objects.count()
    qtd_motoristas = Motorista.objects.count()

    #Contando quantas viagens e seus determinados estado
    qtd_viagens = Viagem.objects.all().count()
    estado_concluido = Viagem.objects.filter(estado='C').count()
    estado_pendente = Viagem.objects.filter(estado='P').count()
    estado_em_viagem = Viagem.objects.filter(estado='E').count()
    estado_atradaso = Viagem.objects.filter(estado='A').count()

    #Criando dicionario para realizar o mapeamento dos itens
    conteudo = {
        'qtd_pacientes': qtd_pacientes,
        'qtd_motoristas': qtd_motoristas,
        'qtd_viagens': qtd_viagens,
        'estado_concluido': estado_concluido,
        'estado_pendente': estado_pendente,
        'estado_em_viagem': estado_em_viagem,
        'estado_atradaso': estado_atradaso,
    }

    #renderizando o template
    return render(request, 'index.html', context=conteudo)


