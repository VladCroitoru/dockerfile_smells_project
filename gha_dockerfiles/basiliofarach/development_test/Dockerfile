FROM python:3.9.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY requirements.txt /app/

RUN pip3 install -r requirements.txt
COPY . /app/
