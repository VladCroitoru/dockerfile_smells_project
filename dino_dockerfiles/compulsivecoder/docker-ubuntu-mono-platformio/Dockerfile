FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install python-software-properties software-properties-common && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN add-apt-repository ppa:saiarcot895/myppa && \
  apt-get update && \
  apt-get -y install apt-fast && \
  apt-fast update

RUN apt-fast install -y curl git wget unzip mono-complete mono-xsp4 python && \
  apt-fast clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN python -c "$(curl -fsSL https://raw.githubusercontent.com/platformio/platformio/develop/scripts/get-platformio.py)"
