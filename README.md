# Project: Tourism API

REST service with authentication, throttling, automated deployment on AWS via GitHub Actions, orchestration with Kubernetes and infrastructure provisioning with Terraform to ensure scalability and automation of the environment.

## 🛠️ Project Resources:

- Decorators
- Unit Tests 
- Throttle
- Pagination
- Filter
- Docker 
- Kubernetes
- CI/CD: GitHub Actions
- Terraform: AWS (in progress)
- Clean Architecture
- Deploy: AWS or Heroku

## Running the Project

## Django:

### Install dependencies:

    pip install -r requirements.txt

### Run server: 

    python manage.py runserver

## Docker:

### Image:

    docker build -t joaodev599/python-api:v2 .

### Container:

    docker container run -d -p 8000:8000 --name python-api joaodev599/python-api:v2

### Run 
    
    docker start python-api

## Tests:

### Atrações Test:

    python manage.py test atracoes


