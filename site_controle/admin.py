from django.contrib import admin

#Importando os models
from site_controle.models import Motorista, Viagem, Paciente

#Possibilitando com que o admin possa fazer o registro no painel de administração
admin.site.register(Motorista)
admin.site.register(Viagem)
admin.site.register(Paciente)

