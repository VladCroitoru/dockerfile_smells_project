FROM python:3.9.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/c-ads

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install --upgrade pip
RUN apk add zlib-dev jpeg-dev gcc musl-dev # For Pillow library.
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/c-ads
