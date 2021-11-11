FROM ubuntu:latest
MAINTAINER kaosf <ka.kaosf@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get install -y xfce4 tightvncserver language-pack-ja xfonts-base fonts-vlgothic && \
  apt-get clean && \
  rm -rf /var/lib/apt/*
