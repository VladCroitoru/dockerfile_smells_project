FROM python:3
EXPOSE 8000
ENV PYTHONUNBUFFERED 1

RUN pip install hug slackclient -U && mkdir /app
WORKDIR /app

COPY . /app/

