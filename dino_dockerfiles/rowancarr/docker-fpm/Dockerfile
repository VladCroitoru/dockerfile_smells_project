FROM ruby:latest
RUN gem install fpm

## Setup for RPM build
RUN apt-get update \
    && apt-get install -y rpm \
    && apt-get clean

## Setup fro python rpm build
RUN apt-get update \
    && apt-get install -y python-setuptools python-dev libxml2-dev libxslt-dev \
    && apt-get clean

USER root
WORKDIR /src

ENTRYPOINT ["/usr/local/bundle/bin/fpm"]
