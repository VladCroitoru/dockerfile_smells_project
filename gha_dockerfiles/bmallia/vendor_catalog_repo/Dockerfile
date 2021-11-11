FROM python:3.9.6-alpine

##dont generate pyc files
ENV PYTHONDONTWRITEBYTECODE 1
##message log dont stand in buffer
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app
