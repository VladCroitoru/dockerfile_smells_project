FROM python:2.7-alpine

MAINTAINER Surisetty, Naresh <naresh@naresh.co>

ENV ORACLE_HOME /opt/oracle/instantclient_12_1
ENV LD_RUN_PATH=$ORACLE_HOME

COPY instantclient/* /tmp/

RUN set -ex \
        && apk add --no-cache --virtual .run-deps \
                bash \
                postgresql \
                postgresql-libs \
        && apk add --no-cache --virtual .build-deps \
                gcc \
                g++ \
                unzip \
                libc-dev \
                unixodbc-dev \
                musl-dev \
                openssl \
                postgresql-dev \
        && mkdir -p /opt/oracle \
        && unzip "/tmp/instantclient*.zip" -d /opt/oracle \
        && ln -s $ORACLE_HOME/libclntsh.so.12.1 $ORACLE_HOME/libclntsh.so \
        && pip --no-cache-dir install \
                psycopg2 \
                cx_Oracle \
        && apk del .build-deps
