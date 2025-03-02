# Projeto: API Turismo


## Recursos do Projeto:

- Testes Unitários
- Throttle
- Paginação
- Docker

## Rodando o Projeto:

### Sem Docker:

    pip install -r requirements.txt

    python manage.py runserver

### Com Docker:

    docker build -t <appName> .

    docker run -p 8000:8000 <appName>
