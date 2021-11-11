FROM python:3.9-slim

RUN pip3 install pipenv
RUN apt-get update -y && apt-get install -y curl git postgresql-client
WORKDIR /app
COPY . /app
RUN pipenv install --system --deploy