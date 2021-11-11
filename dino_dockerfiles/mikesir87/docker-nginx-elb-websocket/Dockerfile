FROM nginx:1.11.1

MAINTAINER Michael Irwin <mikesir87@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

ENV CONFD_VERSION 0.10.0

ADD etc/confd /etc/confd

ADD confd/confd-0.10.0-linux-amd64 /bin/confd

RUN mkdir /config-overrides

WORKDIR /nginx

ADD boot boot

CMD ["./boot"]
