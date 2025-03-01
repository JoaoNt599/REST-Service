# API Turismo


## Rodando o projeto:

### Inicializando projeto com Docker:

    docker build -t docker-python .
    docker run -p 8080:8000 docker-python

### Startando container criado:

    docker start 6f3c

### Parando o container em execução:

    docker stop 6f3c

### Logs do container:

    docker logs 6f3c