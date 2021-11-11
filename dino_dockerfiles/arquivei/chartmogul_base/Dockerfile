# building the image for the chartmogul connection docker container
# > docker build -t docker.chartmogul.server .

FROM debian:jessie
MAINTAINER Dev Arquivei <devops@arquivei.com.br>

USER root

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y locales

## Set LOCALE to UTF8
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN apt-get update && \
    apt-get install -y curl software-properties-common

RUN curl -L -O https://download.elastic.co/beats/filebeat/filebeat_1.2.3_amd64.deb \
    && dpkg -i filebeat_1.2.3_amd64.deb \
    && apt-get update \
    && apt-get install -y python-software-properties locales \
        lynx-cur git build-essential openjdk-7-jdk python3.4 python3.4-dev \
    && mkdir -p /etc/pki/tls/certs/ \
    && curl -L https://raw.githubusercontent.com/cloudflare/cfssl_trust/master/intermediate_ca/COMODORSADomainValidationSecureServerCA.crt > /etc/pki/tls/certs/logzioCA.crt

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN set -x \
    && apt-get update \
    && apt-get install -y \
        python3-pip libpq-dev \
    && pip3 install pymongo \
    && pip3 install psycopg2 \
    && pip3 install pytz \
    && pip3 install iso8601

WORKDIR /media
