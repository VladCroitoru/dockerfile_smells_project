# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUM pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "test_numero_natural.py"]
