FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
ADD . /usr/src/app
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

COPY . /usr/src/app/

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt