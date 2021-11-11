FROM ubuntu:latest

MAINTAINER BYUN Sangpil <sangpire@gmail.com>

RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/' /etc/apt/sources.list \
  && apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y\
    vim-nox\
    curl\
    wget\
    man\
    zip\
    git\
    tree

RUN mkdir -p /play
WORKDIR /play

CMD ["cat"]
