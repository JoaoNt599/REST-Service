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

    docker build -t api -f docker/Dockerfile .

    docker run -p 8000:8000 -v C:/Users/joaon/Desktop/Python/Projeto:/app api

    docker start <id>

