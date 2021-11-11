## Django 1.6.11 ##
FROM python:2-alpine3.7 AS django-1.6.11

RUN mkdir -p /usr/src/django
WORKDIR /usr/src/django

RUN set -ex; \
    \
    pip install sphinx==1.5.6; \
    \
    apk add --no-cache \
        make \
        wget \
    ;

RUN wget -O django.tar.gz https://github.com/django/django/archive/1.6.11.tar.gz; \
    tar -xzf django.tar.gz --strip-components=1; \
    rm django.tar.gz

RUN make -C docs html


## Django Rest Framework 2.4.8 ##
FROM python:2-alpine3.7 AS djangorestframework-2.4.8

RUN mkdir -p /usr/src/djangorestframework
WORKDIR /usr/src/djangorestframework

RUN set -ex; \
    \
    apk add --no-cache \
        wget \
    ;

RUN wget -O djangorestframework.tar.gz https://github.com/encode/django-rest-framework/archive/2.4.8.tar.gz; \
    tar -xzf djangorestframework.tar.gz --strip-components=1; \
    rm djangorestframework.tar.gz; \
    pip install -r docs/requirements.txt

ADD patches/djangorestframework.patch .
RUN patch < djangorestframework.patch

RUN python mkdocs.py


## Primary nginx server ##
FROM nginx:1.12-alpine

ADD nginx.conf /etc/nginx/conf.d/default.conf
RUN rm /usr/share/nginx/html/*

RUN mkdir -p /usr/share/nginx/html/django/1.6.11/
COPY --from=django-1.6.11 /usr/src/django/docs/_build/html/ /usr/share/nginx/html/django/1.6.11/

RUN mkdir -p /usr/share/nginx/html/djangorestframework/2.4.8/
COPY --from=djangorestframework-2.4.8 /usr/src/djangorestframework/html/ /usr/share/nginx/html/djangorestframework/2.4.8/
