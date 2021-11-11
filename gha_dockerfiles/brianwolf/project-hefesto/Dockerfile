FROM python:3.9-slim

ARG ARG_VERSION=local

ENV VERSION=${ARG_VERSION}
ENV PYTHON_HOST=0.0.0.0
ENV PYTHON_PORT=80
ENV TZ America/Argentina/Buenos_Aires

WORKDIR /home/src

RUN apt update
RUN apt install git -y

CMD gunicorn -b ${PYTHON_HOST}:${PYTHON_PORT} --reload app:app

COPY . .
RUN pip install -r requirements.txt --upgrade pip