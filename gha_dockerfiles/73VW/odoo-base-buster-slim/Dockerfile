# syntax=docker/dockerfile:1
FROM python:2.7.18-buster as builder

ENV WORKDIR="/opt/odoo"
ENV VIRTUAL_ENV="$WORKDIR/venv"

RUN apt-get update 
RUN apt-get install -y build-essential
RUN apt-get install -y gcc
RUN apt-get install -y git 
RUN apt-get install -y libevent-dev 
RUN apt-get install -y libkeyutils-dev 
RUN apt-get install -y libldap2-dev 
RUN apt-get install -y libpq-dev 
RUN apt-get install -y libsasl2-dev 
RUN apt-get install -y libssl-dev 
RUN apt-get install -y libxml2-dev 
RUN apt-get install -y libxslt-dev 
RUN apt-get install -y linux-headers-amd64 
RUN apt-get install -y python-lxml
RUN apt-get install -y python-pip 
RUN apt-get install -y python-psycopg2 
RUN apt-get install -y python2-dev 
RUN apt-get install -y virtualenv 
RUN git clone https://github.com/odoo/odoo.git --branch=10.0 --depth=1


RUN virtualenv -p /usr/bin/python2.7 $VIRTUAL_ENV
COPY stack-requirements.txt stack-requirements.txt
RUN $VIRTUAL_ENV/bin/pip install -r stack-requirements.txt
COPY odoo-requirements.txt odoo-requirements.txt
RUN $VIRTUAL_ENV/bin/pip install -r odoo-requirements.txt
RUN $VIRTUAL_ENV/bin/pip install ./odoo

# https://stackoverflow.com/a/10739838/9395299
RUN echo "/usr/local/lib/python2.7/lib-dynload" > $VIRTUAL_ENV/lib/python2.7/site-packages/path.pth 

RUN adduser --disabled-password --gecos '' odoo  
RUN mkdir -p /opt/odoo/current/ 
RUN mkdir -p /opt/odoo/filestore
RUN chown -R odoo:odoo /opt/odoo/

FROM python:2.7.18-slim-buster as image

LABEL \
    maintainer="Mael Pedretti <mael.pedretti@vnv.ch>" \
    org.label-schema.name="Odoo Base (Buster-slim)"\
    org.label-schema.schema-version="1.0" \
    org.label-schema.version="1.0" 

ENV WORKDIR="/opt/odoo"
ENV VIRTUAL_ENV="$WORKDIR/venv" \
    PATH="$WORKDIR/venv/bin:$PATH" 

RUN adduser --disabled-password --gecos '' odoo \
    && apt-get update && apt-get install -y --no-install-recommends\
    node-less \
    python-lxml \
    python-psycopg2 \
    wkhtmltopdf \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false npm \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /var/log/odoo/ && chown -R odoo:odoo /var/log/odoo/ \
    && mkdir -p /var/odoo/ && chown -R odoo:odoo /var/odoo/

COPY --from=builder $WORKDIR $WORKDIR