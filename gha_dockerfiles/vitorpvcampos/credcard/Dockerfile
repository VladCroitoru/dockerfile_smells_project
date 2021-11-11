FROM python:3.9.0-slim
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY here-comes-a-secret-key

WORKDIR /code
COPY manage.py /code
COPY .env /code
COPY Pipfile.lock /code
COPY Pipfile /code

RUN apt-get update && \
    apt-get install -y libpq-dev gcc
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install psycopg2
RUN pipenv install --system --deploy --ignore-pipfile --dev

COPY . /code/