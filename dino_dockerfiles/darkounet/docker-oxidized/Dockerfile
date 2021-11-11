# Jessie Dockerfile
# For oxidized + oxidized-web
# https://github.com/ytti/oxidized
# https://github.com/ytti/oxidized-web
#

FROM debian:jessie

MAINTAINER Antoine GUEVARA <me@antoine-guevara.fr>

ENV HOSTNAME oxidized.docker.lan
ENV DEBIAN_FRONTEND noninteractive
ENV SHELL /bin/bash

RUN apt-get update

RUN apt-get install -y -qq vim ruby ruby-dev libsqlite3-dev libssl-dev pkg-config cmake

RUN gem install oxidized
RUN gem install oxidized-script
RUN gem install oxidized-web

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN rm -rf ~/.config/oxidized/

EXPOSE 8888

VOLUME ["/root/.config/oxidized/"]

ENTRYPOINT ["/usr/local/bin/oxidized"]

CMD ["-d"]
