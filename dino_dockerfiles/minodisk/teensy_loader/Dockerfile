FROM debian:jessie
MAINTAINER Daisuke Mino <daisuke.mino@gmail.com>

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
      build-essential \
      wget \
      ca-certificates \
      unzip \
      libusb-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /teensy_loader
RUN wget https://github.com/PaulStoffregen/teensy_loader_cli/archive/master.zip && \
    unzip master.zip

WORKDIR /teensy_loader/teensy_loader_cli-master
RUN make && \
    mv teensy_loader_cli /usr/local/bin && \
    rm -rf /teensy_loader

WORKDIR /scripts
COPY run.sh ./

WORKDIR /qmk/.build
ENV hex=ergodox_ez_default
ENV mcu=atmega32u4
CMD bash /scripts/run.sh
