FROM ubuntu:18.04

MAINTAINER chinesedewey@gmail.com

ENV DOCKERIZE_VERSION v0.6.1

# We don't want to interact during image builds
ENV DEBIAN_FRONTEND noninteractive

# Set up locales
RUN apt-get update \
    && apt-get install -y locales \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

ENV PATH "${PATH}:/opt/cli_venv/bin"

RUN apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository -y ppa:maxmind/ppa \
  && add-apt-repository -y ppa:deadsnakes/ppa \
  && apt-get update \
  && apt-get install -y \
    curl \
    git-all \
    language-pack-id \
    libcurl4-openssl-dev \
    libffi-dev \
    libjpeg-dev \
    libmaxminddb-dev \
    libmaxminddb0 \
    libmysqlclient-dev \
    libpng-dev \
    libpq-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    mmdb-bin \
    mysql-client \
    ntp \
    postgresql-client \
    python3.6 \
    python3.6-dev \
    python3.6-venv \
    unzip \
    wget \
    zlib1g-dev \
  && apt-get clean

RUN mkdir /usr/share/GeoIP && \
    chmod 755 /usr/share/GeoIP && \
    cd /usr/share/GeoIP/ && \
    wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz && \
    tar xzvf GeoLite2-City.tar.gz && \
    mv GeoLite2-City_*/GeoLite2-City.mmdb GeoIP2-City.mmdb && \
    rm -r GeoLite2-City_* GeoLite2-City.tar.gz && \
    chmod 444 GeoIP2-City.mmdb

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O /usr/local/bin/jq \
  && chmod a+x /usr/local/bin/jq

RUN python3.6 -m venv /opt/cli_venv \
  && /opt/cli_venv/bin/pip install --upgrade pip \
  && /opt/cli_venv/bin/pip install --upgrade awscli requests \
  && rm -r /root/.cache/pip
