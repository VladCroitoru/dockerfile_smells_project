FROM ubuntu:14.04

MAINTAINER Bleno <blenobok@gmail.com>

#  Container do bora hoje admin
#   
#

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y wget tar

RUN  sh -c 'echo deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx > /etc/apt/sources.list.d/nginx.list' \
     && sh -c 'echo deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx >> /etc/apt/sources.list.d/nginx.list' \
     && wget -q -O - http://nginx.org/keys/nginx_signing.key | apt-key add -

RUN apt-get update \
    && apt-get install -y build-essential python3-dev python3-pip python3.4-venv python-virtualenv \
    && apt-get install -y libpq-dev nginx git-core \
    && apt-get install -y python-virtualenv libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

RUN mkdir -p /usr/local/borahoje \
    && cd  /usr/local/borahoje \
    && virtualenv -p python3 ve34 \
    && mkdir -p ve34/src/bora-hoje-admin

## Dependencias bora_hpje
#

RUN /usr/local/borahoje/ve34/bin/pip3 install django \
    && /usr/local/borahoje/ve34/bin/pip3 install djangorestframework \
    && /usr/local/borahoje/ve34/bin/pip3 install psycopg2 \
    && /usr/local/borahoje/ve34/bin/pip3 install gunicorn \
    && /usr/local/borahoje/ve34/bin/pip3 install redis \
    && /usr/local/borahoje/ve34/bin/pip3 install qrcode \
    && /usr/local/borahoje/ve34/bin/pip3 install Pillow \
    && /usr/local/borahoje/ve34/bin/pip3 install -e git+http://github.com/lightbase/liblightbase.git#egg=liblightbase


RUN rm /etc/nginx/conf.d/default.conf \
    && apt-get -y autoclean \
    && apt-get -y autoremove

COPY bora_hoje_admin.conf /etc/nginx/conf.d/bora_hoje_admin.conf

COPY gunicorn.conf /etc/init/gunicorn.conf


EXPOSE 80
