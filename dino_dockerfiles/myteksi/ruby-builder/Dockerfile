FROM ruby:2.4.2-slim

RUN apt-get update && \
  apt-get install -y --no-install-recommends git nodejs \
          libmysqlclient-dev \
          libxml2-dev \
          libxslt-dev && \
  rm -rf /var/lib/apt/lists/*
