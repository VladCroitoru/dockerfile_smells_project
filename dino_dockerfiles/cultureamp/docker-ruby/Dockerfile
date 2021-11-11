FROM ruby:2.3

MAINTAINER Andy Nicholson <andy@cogent.co>

RUN apt-get update

RUN apt-get install -y \
    postgresql-client \
    git \
    wget

RUN cd /tmp && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

RUN pip install awscli

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz
