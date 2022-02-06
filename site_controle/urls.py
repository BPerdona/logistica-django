from unicodedata import name
from django.urls import path
from site_controle import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paciente/', views.PacienteListaView.as_view(), name='pacientes'),
    path('paciente/<int:pk>', views.PacienteDetalheView.as_view(), name='paciente-detalhe'),
]