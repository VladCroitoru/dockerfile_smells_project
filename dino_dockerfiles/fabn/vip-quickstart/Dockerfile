FROM ubuntu:precise

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y git curl puppet sudo wget

RUN git clone https://github.com/Automattic/vip-quickstart.git /srv

WORKDIR /srv

RUN /srv/bin/vip-init --server --domain vip.dev
