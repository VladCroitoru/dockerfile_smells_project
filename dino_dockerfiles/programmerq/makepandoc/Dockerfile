FROM debian:jessie
MAINTAINER Jeff Anderson <jeff@docker.com>

VOLUME [/sources]

RUN apt-get -y update
RUN apt-get -y install pandoc make texlive-full

WORKDIR /sources
CMD make
