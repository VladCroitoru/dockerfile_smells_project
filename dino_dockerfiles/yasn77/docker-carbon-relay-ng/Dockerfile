FROM busybox:ubuntu-14.04
MAINTAINER Yasser Nabi "yassersaleemi@gmail.com"
EXPOSE 2003 2004 8081

RUN mkdir /carbon_spool

ADD ./carbon-relay-ng.ini /carbon-relay-ng.ini
ADD ./carbon-relay-ng_sha9d6e319 /carbon-relay-ng
ADD ./start.sh /start.sh

ENTRYPOINT /start.sh
