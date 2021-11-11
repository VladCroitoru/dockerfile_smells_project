FROM ubuntu:xenial

MAINTAINER Pyro225 <pyro225@gmail.com>

RUN apt-get update \
 && apt-get install -y software-properties-common \
 \
 && apt-add-repository -y ppa:freecad-maintainers/freecad-daily \
 && apt-get update \
 && apt-get install -y freecad-daily \
 \
 && apt-get clean

RUN adduser --disabled-password --quiet --gecos '' freecad
RUN usermod -aG video freecad
USER freecad
CMD freecad-daily
