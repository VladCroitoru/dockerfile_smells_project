FROM debian:stable-slim

LABEL org.label-schema.name="wercker-box-base" \
      org.label-schema.description="General purpose debian based base box for Wercker pipelines with extra tools." \
      org.label-schema.url="https://github.com/jappievw/wercker-box-base" \
      org.label-schema.org.vcs-url="https://github.com/jappievw/wercker-box-base" \
      org.label-schema.org.vcs-type="git" \
      org.label-schema.schema-version="1.0"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get -y install \
    git \
    curl \
    netcat

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
