FROM debian:squeeze

MAINTAINER Jared Feng <github@indeed.moe>

# Debian squeeze has reached end of life thus have to be found in archive.
RUN sed -i -e 's/httpredir.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i -e '/squeeze-updates/d' /etc/apt/sources.list

RUN apt-get -o Acquire::Check-Valid-Until=false update && \
    apt-get upgrade -y && \
    apt-get install -y transmission-daemon

ADD files/transmission-daemon /etc/transmission-daemon
ADD files/run_transmission.sh /run_transmission.sh

RUN mkdir -p /var/lib/transmission-daemon/incomplete && \
    mkdir -p /var/lib/transmission-daemon/downloads && \
    chown -R debian-transmission:debian-transmission /var/lib/transmission-daemon && \
    chown -R debian-transmission:debian-transmission /etc/transmission-daemon    

VOLUME ["/var/lib/transmission-daemon/downloads"]
VOLUME ["/var/lib/transmission-daemon/incomplete"]
VOLUME ["/etc/transmission-daemon/resume"]
VOLUME ["/etc/transmission-daemon/torrents"]

EXPOSE 9091
EXPOSE 12345

USER debian-transmission

CMD ["/run_transmission.sh"]
