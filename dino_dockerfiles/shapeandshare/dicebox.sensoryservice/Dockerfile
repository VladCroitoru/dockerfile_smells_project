# https://hub.docker.com/r/tiangolo/uwsgi-nginx/
FROM tiangolo/uwsgi-nginx:python2.7

WORKDIR /app

COPY ./app /app
COPY ./dicebox/dicebox /app/dicebox
COPY ./dicebox/dicebox.config /app

RUN pip install -r requirements.txt \
    && useradd -M -U -u 1000 sensoryservice \
    && chown -R sensoryservice /app

EXPOSE 80
