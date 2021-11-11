FROM ubuntu:14.04.5

MAINTAINER chinesedewey@gmail.com

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV DOCKERIZE_VERSION v0.4.0

ENV PATH "${PATH}:/opt/aws_cli_venv/bin"

RUN apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository -y ppa:maxmind/ppa \
  && add-apt-repository -y ppa:fkrull/deadsnakes \
  && apt-get install -y wget \
  && wget -qO - http://packages.confluent.io/deb/3.1/archive.key | sudo apt-key add - \
  && add-apt-repository -y "deb [arch=amd64] http://packages.confluent.io/deb/3.1 stable main" \
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
    librdkafka++1 \
    librdkafka-dev \
    librdkafka-dev \
    librdkafka1 \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    mmdb-bin \
    mysql-client \
    postgresql-client \
    python3.6 \
    python3.6-dev \
    python3.6-venv \
    zlib1g-dev \
  && apt-get clean

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
  && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O /usr/local/bin/jq \
  && chmod a+x /usr/local/bin/jq

RUN python3.6 -m venv /opt/aws_cli_venv \
  && /opt/aws_cli_venv/bin/pip install --upgrade awscli \
  && rm -r /root/.cache/pip
