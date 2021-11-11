FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apt update \
    && apt install -y libpq-dev gcc

RUN pip install psycopg2

COPY . /code/