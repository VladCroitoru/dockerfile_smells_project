# Jessie Dockerfile
# with mcabber package
# Small XMPP console client
# http://lilotux.net/~mikael/mcabber/

FROM debian:jessie

MAINTAINER Antoine GUEVARA <me@antoine-guevara.fr>

ENV HOSTNAME mcabber.docker.lan
ENV DEBIAN_FRONTEND noninteractive
ENV SHELL /bin/bash

ENV JABBER_USERNAME user@jabber.example.com
ENV JABBER_SERVER jabber.example.com
ENV LANG C.UTF-8

RUN useradd -ms /bin/bash mcabber_client

RUN apt-get update

RUN apt-get install -y -qq mcabber

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir /home/mcabber_client/.mcabber

ADD ./conf/.mcabber/mcabberrc.example /home/mcabber_client/.mcabber/mcabberrc.example

ADD ./scripts /home/mcabber_client/scripts/

WORKDIR /home/mcabber_client/.mcabber

RUN /home/mcabber_client/scripts/mcabber_config.sh

VOLUME ["/home/mcabber_client/.mcabber", "/home/mcabber_client/scripts/"]
USER mcabber_client

CMD ["/home/mcabber_client/scripts/mcabber_config.sh"]
