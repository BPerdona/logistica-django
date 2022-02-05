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

![diagram_de_classe](https://github.com/BPerdona/logistica-django/blob/main/Diagrama_Classes.png)

## Objetivos para obtenção de nota

- (1 ponto) 1. Crie um projeto do Django e implemente os modelos (models) do diagrama criado, definindo corretamente os relacionamentos;
- (1 ponto) 2. Utilizando a extensão de templates do Django, crie um layout para sua aplicação web;
- (1 ponto) 3. Crie uma página principal que apresente o número de registros gravados em cada um dos seus models;
- (1 ponto) 4. Crie uma página que apresente uma lista dos registros do model principal do seu sistema;
- (1 ponto) 5. Utilizando formulários, crie um CRUD (páginas de detalhes, criação, edição e exclusão) dos registros do model principal do seu sistema;
- (1 ponto) 6. Implemente a autenticação do Django, criando as páginas de login e logout;
- (1 ponto) 7. Implemente a autorização, de forma que apenas um usuário que possua uma determinada permissão possa realizar as operações de CRUD dos registros do model principal;
- (1 ponto) 8. Coloque a aplicação em produção (deploy) no PythonAnywhere ou no Heroku (ou em algum outro serviço de hospedagem que preferir).

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
