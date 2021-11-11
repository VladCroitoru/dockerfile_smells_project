############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

FROM phusion/baseimage:0.9.18

MAINTAINER Maintaner Name

RUN apt-get update && \
  apt-get install -y tar dovecot-imapd && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 143

VOLUME /home

CMD ["/sbin/my_init"]

COPY resources/dovecot.conf /etc/dovecot/dovecot.conf
COPY resources/10-mail.conf /etc/dovecot/conf.d/10-mail.conf

RUN mkdir /etc/service/dovecot

COPY resources/dovecot.sh /etc/service/dovecot/run
