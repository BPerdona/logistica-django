from django.db import models
from django.urls import reverse

class Paciente(models.Model):
    
    nome = models.CharField(max_length=150)
    data_nasc = models.DateField(null=True, blank=True)
    rg = models.CharField(max_length=11)
    cns = models.CharField(max_length=18)
    telefone = models.CharField(max_length=20)
    local_espera = models.TextField(max_length=1000, help_text="Entre com uma breve descrição do local de espera.")

    def get_absolute_url(self):
        return reverse('paciente-detalhe', args=[str(self.id)])

    def __str__(self):
        return self.nome

    class Meta:
        ordering=['nome']
        permissions = (("pode_manipular_paciente", "Manipula o cadastro de pacientes."),("pode_criar_paciente", "Possibilita a criação de pacientes."),)

class Motorista(models.Model):

    nome = models.CharField(max_length=150)
    rg = models.CharField(max_length=11)
    data_nasc = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Viagem(models.Model):

    data_viagem = models.DateField(null=True, blank=True)
    destino = models.CharField(max_length=200)
    saida = models.CharField(max_length=6)
    paciente = models.ManyToManyField(Paciente, help_text="Selecione os pacientes que iram nessa viagem.")
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True)

    ESTADO_VIAGEM = (
        ('C', 'Concluída'),
        ('P','Pendente'),
        ('E','Em Viagem'),
        ('A', 'Atrasado'),
    )

    estado = models.CharField(
        max_length=1,
        choices=ESTADO_VIAGEM,
        blank=True,
        default='P',
        help_text="Situação da Viagem",
    )

    class Meta:
        ordering = ['data_viagem']
        permissions = (("pode_manipular_viagem", "Manipula o cadastro de viagens."),("pode_criar_viagem", "Possibilita a criação de viagens."))

    def get_absolute_url(self):
        return reverse('viagem-detalhe', args=[str(self.id)])

    def __str__(self):
        return f'Viagem para {self.destino}| Dia: {self.data_viagem}| Saida: {self.saida}'