FROM python:3.8-slim-buster

WORKDIR /app

ENV DJANGO_DEBUG=True
ENV DJANGO_ALLOWED_HOSTS=0.0.0.0,localhost
ENV DJANGO_SECRET_KEY='django-insecure-e$8b9xvyjpr^2%3@k)6*^!+@56al)x1-31vz8k6(^ilwow)4(9'

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
