FROM ubuntu:16.04
ARG DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/^#\s*\(deb.*multiverse\)$/\1/g' /etc/apt/sources.list
RUN sed -i 's/^\s*\(deb\s*.* xenial universe\)$/\1 multiverse/g' /etc/apt/sources.list

RUN dpkg --add-architecture i386 && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y apt-utils debconf-utils ca-certificates

ADD src/steamcmd-selections steamcmd-selections
RUN debconf-set-selections steamcmd-selections && \
    apt-get install -y steamcmd && \
    ln -s /usr/games/steamcmd /usr/bin/steamcmd && \
    rm steamcmd-selections

RUN apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt/
RUN mkdir -p /opt/l4d2/game/left4dead2/cfg/
ADD src/l4d2/start-l4d2.sh /opt/l4d2/start-l4d2.sh
ADD src/l4d2/l4d2-steamcmd-script /opt/l4d2/l4d2-steamcmd-script
ADD src/l4d2/server.cfg /opt/l4d2/game/left4dead2/cfg/server.cfg
RUN chmod 0555 /opt/l4d2/start-l4d2.sh

VOLUME ["/var/log/", "/opt/l4d2/"]
EXPOSE 27015-27020 27015-27020/udp
ENTRYPOINT ["/opt/l4d2/start-l4d2.sh"]
