from unicodedata import name
from django.urls import path
from site_controle import views

urlpatterns = [
    path('', views.index, name='index'),
]

#URLs referente ao CRUD de Paciente
urlpatterns += [
    path('paciente/', views.PacienteListaView.as_view(), name='pacientes'),
    path('paciente/<int:pk>', views.PacienteDetalheView.as_view(), name='paciente-detalhe'),
    path('paciente/create/', views.PacienteCreate.as_view(), name="paciente-create"),
    path('paciente/<int:pk>/update/', views.PacienteUpdate.as_view(), name="paciente-update"),
    path('paciente/<int:pk>/delete/', views.PacienteDelete.as_view(), name="paciente-delete"),
]

#URLs refetente ao CRUD de Viagem
urlpatterns += [
    path('viagem/', views.ViagemListaView.as_view(), name="viagens"),
    path('viagem/<int:pk>', views.ViagemDetalheView.as_view(), name="viagem-detalhe"),
    path('viagem/create/', views.ViagemCreate.as_view(), name="viagem-create"),
    path('viagem/<int:pk>/update/', views.ViagemUpdate.as_view(), name="viagem-update"),
    path('viagem/<int:pk>/delete/', views.ViagemDelete.as_view(), name="viagem-delete"),
]