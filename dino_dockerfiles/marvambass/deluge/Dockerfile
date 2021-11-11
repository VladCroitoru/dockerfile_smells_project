FROM ubuntu:14.04
MAINTAINER MarvAmBass

RUN apt-get update; apt-get install -y \
    deluged \
    deluge-web

ADD entrypoint.sh /opt/entrypoint.sh
RUN chmod a+x /opt/entrypoint.sh

VOLUME ["/data"]
VOLUME ["/downloads"]

EXPOSE 53160
EXPOSE 53160/udp

EXPOSE 8112
EXPOSE 58846

CMD ["/opt/entrypoint.sh"]
