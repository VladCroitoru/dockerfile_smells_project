FROM ubuntu:trusty

MAINTAINER guyschaos@gmail.com


COPY sources.list.trusty /etc/apt/sources.list
RUN apt-get update \
        && apt-get install -y  wget libdbi-perl libdbd-mysql-perl libterm-readkey-perl \
        libio-socket-ssl-perl libmysqlclient18 libio-socket-ip-perl libio-socket-inet6-perl \
        libnet-libidn-perl libsocket6-perl libnet-ssleay-perl mysql-common mysql-client-5.6 \
        && apt-get clean

RUN wget percona.com/get/percona-toolkit.deb

RUN dpkg -i percona-toolkit.deb