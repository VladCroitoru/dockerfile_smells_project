FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y bundler zlib1g-dev python libcurl3

WORKDIR /site

EXPOSE 4000
CMD make deps serve
