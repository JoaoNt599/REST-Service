# Projeto: API Turismo


## Recursos do Projeto:

- Testes Unitários
- Throttle
- Paginação
- Docker
- Clean Architecture


## Rodando o Projeto:

### Sem Docker:

    pip install -r requirements.txt

    python manage.py runserver

### Com Docker:

    docker build -t joaodev599/python-api:v2 .

    docker container run -d -p 8000:8000 --name python-api joaodev599/python-api:v2

    docker start python-api

