FROM ubuntu:yakkety
MAINTAINER Thomas Boerger <thomas@webhippie.de>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
  apt-get install -y \
    ca-certificates \
    bash \
    bash-completion \
    ncurses-base \
    vim \
    curl \
    procps && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

ADD rootfs /

ENV CRON_ENABLED false
ENV TERM xterm
CMD ["bash"]
