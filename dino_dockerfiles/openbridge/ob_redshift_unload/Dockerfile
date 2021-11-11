FROM python:2.7.13-alpine3.6
MAINTAINER Thomas Spicer <thomas@openbridge.com>

ENV LANG C.UTF-8

ENV PY_DEPS \
      curl \
      postgresql-dev \
      libc-dev \
      linux-headers \
      build-base \
      gcc \
      musl-dev
RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && apk update \
    && apk add --update --no-cache --virtual .build-deps \
       $PY_DEPS \
    && update-ca-certificates \
    && curl -fSL https://s3.amazonaws.com/redshift-downloads/redshift-ssl-ca-cert.pem > /redshift-ssl-ca-cert.pem \
    && apk add --update --virtual .python-deps \
        postgresql-client \
        bash \
        curl \
    && pip install --no-cache-dir awscli setuptools psycopg2 python-dateutil argparse \
    && mkdir /root/.aws \
    && rm -rf /usr/src/python ~/.cache \
    && rm -Rf /tmp/* \
    && apk del .build-deps
COPY . /
CMD ["python2"]
