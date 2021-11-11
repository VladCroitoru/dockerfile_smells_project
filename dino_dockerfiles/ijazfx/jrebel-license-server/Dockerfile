FROM openjdk:8u121-jre

MAINTAINER SG Finans <frontutvikling@sgfinans.no>

ENV VERSION="3.3.0"
RUN mkdir /jrebel

RUN wget -O /tmp/license-server.zip -q "http://dl.zeroturnaround.com/license-server/license-server-${VERSION}.zip"
RUN unzip -u -o /tmp/license-server.zip -d /jrebel

EXPOSE 9000

VOLUME ["/jrebel/license-server/data/"]


CMD ["/jrebel/license-server/bin/license-server.sh", "run"]
