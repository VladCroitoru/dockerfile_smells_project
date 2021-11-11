FROM java:8

MAINTAINER cgo IT <info@cgo-it.de>

ENV VERSION="3.3.9"
RUN mkdir /jrebel

RUN wget -O /tmp/license-server.zip -q "http://dl.zeroturnaround.com/license-server/license-server-${VERSION}.zip"
RUN unzip -u -o /tmp/license-server.zip -d /jrebel

EXPOSE 9000

VOLUME ["/jrebel/license-server/data/"]


CMD ["/jrebel/license-server/bin/license-server.sh", "run"]
