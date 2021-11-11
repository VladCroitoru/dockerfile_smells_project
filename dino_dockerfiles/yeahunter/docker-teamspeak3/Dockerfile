FROM ubuntu

MAINTAINER Invisible <yeahunter@gmail.com>

ENV TEAMSPEAK_URL http://dl.4players.de/ts/releases/3.0.11.3/teamspeak3-server_linux-amd64-3.0.11.3.tar.gz

ADD ${TEAMSPEAK_URL} /opt/

ADD start-teamspeak3.sh /start-teamspeak3

EXPOSE 9987/udp 10011 30033

VOLUME ["/data"]
WORKDIR /data
CMD ["/start-teamspeak3"]
