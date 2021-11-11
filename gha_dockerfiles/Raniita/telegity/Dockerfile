FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update && apt-get install -y ca-certificates

ENV STATIC_PATH /app/app/static
ENV UWSGI_INI /app/uwsgi.ini
ENV NGINX_WORKER_PROCESSES auto

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app