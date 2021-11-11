FROM debian:stretch
MAINTAINER Anton Yugov <i@ayugov.ru>

ENV DEBIAN_FRONTEND noninteractive

ADD sources.list /etc/apt/sources.list

RUN apt-get update -y
RUN apt-get dist-upgrade -y
RUN apt-get install curl -y
RUN apt-get install git -y

RUN git config --global http.sslverify false
ADD nginx.list /etc/apt/sources.list.d/nginx.list

ADD nginx-module.patch /tmp/nginx-module.patch

WORKDIR /tmp

RUN mkdir /target

ADD build.sh /build.sh

VOLUME [ "/target" ]

ENTRYPOINT [ "/build.sh" ]
