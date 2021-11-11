FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && pip install psycopg2

RUN mkdir /backend

WORKDIR /backend

COPY requirements.txt /backend/

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install Pillow
RUN pip install -r requirements.txt

COPY . /backend/
EXPOSE 3333