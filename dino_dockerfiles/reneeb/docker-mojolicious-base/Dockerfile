FROM alpine:latest
MAINTAINER Renee Baecker

COPY cpanfile /
ENV EV_EXTRA_DEFS -DEV_NO_ATFORK

RUN apk update && \
  apk add perl perl-io-socket-ssl perl-dev g++ make wget curl && \
  curl -L https://cpanmin.us | perl - App::cpanminus && \
  cpanm --installdeps . -M https://cpan.metacpan.org && \
  apk del g++ make wget curl && \
  rm -rf /root/.cpanm/* /usr/local/share/man/*

RUN apk add shadow

RUN groupadd mojolicious && useradd -m -g mojolicious mojolicious
