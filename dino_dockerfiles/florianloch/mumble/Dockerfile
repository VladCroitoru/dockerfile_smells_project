FROM phusion/baseimage:latest
MAINTAINER Florian Loch <florian.loch@gmail.com>

RUN add-apt-repository ppa:mumble/release \
 && apt-get update \
 && apt-get install -y mumble-server

RUN mkdir /data
RUN mkdir /config

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ./mumble-server.ini /default-mumble-server.ini

RUN mkdir /etc/service/mumbled
ADD mumbled.sh /etc/service/mumbled/run

VOLUME /data
VOLUME /config

EXPOSE 64738/udp
EXPOSE 64738/tcp

CMD ["/sbin/my_init"]
