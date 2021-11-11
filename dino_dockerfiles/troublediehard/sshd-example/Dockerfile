FROM ubuntu

MAINTAINER Dmytro Portenko <dvportenko@gmail.com>

RUN apt-get update && apt-get install -y openssh-server

RUN mkdir -p /var/run/sshd
ONBUILD ADD sshd_config /etc/ssh/sshd_config

CMD /usr/sbin/sshd -D

USER nobody
WORKDIR /tmp
ENV foobar "Hello Worldik"

EXPOSE 2222
