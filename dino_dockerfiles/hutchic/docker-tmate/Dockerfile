FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

RUN apt-get update \
    && apt-get install -y curl openssh-client tmate iputils-ping vim

RUN curl -fsSL get.docker.com -o get-docker.sh \
    && sh get-docker.sh

RUN curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

ADD entrypoint.sh /root/entrypoint.sh

EXPOSE 8080
WORKDIR /root

ENTRYPOINT ["/root/entrypoint.sh"]