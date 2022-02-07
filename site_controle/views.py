from ast import Del
from dataclasses import field, fields
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
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

class PacienteListaView(generic.ListView):
    
    model = Paciente

class PacienteDetalheView(generic.DetailView):
    
    model = Paciente

class ViagemListaView(generic.ListView):

    model = Viagem

class ViagemDetalheView(generic.DetailView):

    model = Viagem

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PacienteCreate(PermissionRequiredMixin, CreateView):

    permission_required = 'site_controle.pode_manipular_paciente'
    model = Paciente
    fields = '__all__'

class PacienteUpdate(PermissionRequiredMixin, UpdateView):

    permission_required = 'site_controle.pode_manipular_paciente'
    model = Paciente
    fields = ['nome', 'data_nasc', 'rg', 'cns', 'telefone', 'local_espera']

class PacienteDelete(PermissionRequiredMixin, DeleteView):

    permission_required = 'site_controle.pode_manipular_paciente'
    model = Paciente
    success_url =  reverse_lazy('pacientes')


class ViagemCreate(PermissionRequiredMixin, CreateView):

    permission_required = 'site_controle.pode_manipular_viagem'
    model = Viagem
    fields = '__all__'

class ViagemUpdate(PermissionRequiredMixin, UpdateView):

    permission_required = 'site_controle.pode_manipular_viagem'
    model = Viagem
    fields = ['data_viagem', 'destino', 'saida', 'paciente', 'motorista', 'estado']

class ViagemDelete(PermissionRequiredMixin, DeleteView):

    permission_required = 'site_controle.pode_manipular_viagem'
    model = Viagem
    success_url = reverse_lazy('viagens')