# Dockerfile for building of SISO application

FROM ruby:2.2.4
MAINTAINER Roy Kokkelkoren <roy.kokkelkoren@gmail.com>

RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/siso
COPY . /usr/src/siso

WORKDIR /usr/src/siso
RUN bin/setup

EXPOSE 3000
CMD ["bin/run"]