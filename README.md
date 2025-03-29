# Project: Tourism API


## 🛠️ Project Resources:

- Unit Tests 
- Throttle
- Pagination
- Docker 
- Kubernetes
- CI/CD: GitHub Actions
- Terraform: AWS (in progress)
- Clean Architecture
- Deploy: AWS or Heroku

## Running the Project:

### Django:

    pip install -r requirements.txt

    python manage.py runserver

### With Docker:

    docker build -t joaodev599/python-api:v2 .

    docker container run -d -p 8000:8000 --name python-api joaodev599/python-api:v2

    docker start python-api

