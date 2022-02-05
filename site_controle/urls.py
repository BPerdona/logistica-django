from django.urls import path
from site_controle import views

urlpatterns = [
    path('', views.index, name='index')
]