# Tutorial MDN Django

**O objetivo é desenvolver um sistema web para gerenciamento de pacientes e viagens para o setor de logistica da prefeitura de Canoinhas.**

Contendo os seguintes funcionamentos:

- Cadastrar Pacientes;
- Consultar Pacientes;
- Cadastrar Motorista;
- Consultar Motorista;
- Cadastrar viagens;
- Consultar Viagens.

## Diagrama de classe

![diagram_de_classe](Diagrama_Classes)

## Requerimentos

- Python 3 ou superior

## Para utilizar o projeto

Utilize os códigos abaixo na linha de comando adaptando para seu sistema:

```
git clone https://github.com/BPerdona/logistica-django.git
```

```
cd <caminho da pasta após extrair>
```

```
python -m venv <nome da sua venv>
```

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

```
python manage.py collectstatic
```

```
python manage.py migrate
```

## Para iniciar o servidor local

```
python3 manage.py runserver
```
