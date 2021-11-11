FROM python:3.9.7

LABEL Side="backend"

COPY . /code

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

RUN mkdir static

RUN chmod +x docker_django/migrate.sh

# auto migrations
CMD ["sh", "docker_django/migrate.sh"]