FROM python:3.9-alpine3.14

ARG ARG_VERSION=local

ENV VERSION=${ARG_VERSION}
ENV PYTHON_HOST=0.0.0.0
ENV PYTHON_PORT=80
ENV TZ America/Argentina/Buenos_Aires

CMD gunicorn -b ${PYTHON_HOST}:${PYTHON_PORT} app:app

WORKDIR /home/src

COPY . .
RUN pip install -r requirements.txt --upgrade pip
