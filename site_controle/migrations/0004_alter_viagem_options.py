# Generated by Django 4.0 on 2022-02-07 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_controle', '0003_alter_paciente_options_alter_viagem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viagem',
            options={'ordering': ['data_viagem'], 'permissions': (('pode_manipular_viagem', 'Manipula o cadastro de viagens.'), ('pode_criar_viagem', 'Possibilita a criação de viagens.'))},
        ),
    ]