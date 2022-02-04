from django.db import models

class Paciente(models.Model):
    
    nome = models.CharField(max_length=150)
    data_nasc = models.DateField(null=True, blank=True)
    rg = models.CharField(max_length=11)
    cns = models.CharField(max_length=18)
    telefone = models.CharField(max_length=20)
    local_espera = models.TextField(max_length=1000, help_text="Entre com uma breve descrição do local de espera.")

    def __str__(self):
        return self.nome

class Motorista(models.Model):

    nome = models.CharField(max_length=150)
    rg = models.CharField(max_length=11)
    data_nasc = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Viagem(models.Model):

    data_viagem = models.DateField(null=True, blank=True)
    destino = models.CharField(max_length=200)
    saida = models.CharField(max_length=6, help_text="HH:MM")
    paciente = models.ManyToManyField(Paciente, help_text="Selecione os pacientes que iram nessa viagem.")
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True)

    ESTADO_VIAGEM = (
        ('C', 'Concluída'),
        ('P','Pendente'),
        ('E','Em Viagem')
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

    def __str__(self):
        return self.data_viagem