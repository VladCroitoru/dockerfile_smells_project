FROM alpine:latest

MAINTAINER PivStone<PivStone@gmail.com>

EXPOSE 5511

ENV APP_HOME /srv/andromeda
ENV DJANGO_SETTINGS_MODULE andromeda.settings.prodn

RUN apk update
RUN apk add nginx git bash
RUN apk add openssl libc-dev python3-dev gcc
RUN rm -rf /var/cache/apk/*

COPY . ${APP_HOME}
VOLUME ${APP_HOME}/etc
VOLUME ${APP_HOME}/data
WORKDIR ${APP_HOME}

RUN pip3 install -r requirements/production.txt -U

COPY etc/andromeda.nginx.conf /etc/nginx/server/
COPY etc/alpine.nginx.conf /etc/nginx

CMD ["/srv/andromeda/entrypoint.sh"]
