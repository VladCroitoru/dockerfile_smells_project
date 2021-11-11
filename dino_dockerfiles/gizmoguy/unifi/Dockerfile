FROM ubuntu:16.04

VOLUME ["/var/lib/unifi"]

ENV DEBIAN_FRONTEND noninteractive

RUN echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" \
  > /etc/apt/sources.list.d/100-ubnt.list

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50

RUN apt-get -q update && \
    apt-get install -qy supervisor unifi && \
    apt-get -q clean && \
    rm -rf /var/lib/apt/lists/*

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD system.properties /usr/lib/unifi/data/system.properties

WORKDIR /var/lib/unifi

EXPOSE 80/tcp 8880/tcp 443/tcp 8843/tcp 3478/udp

CMD ["/usr/bin/supervisord"]
