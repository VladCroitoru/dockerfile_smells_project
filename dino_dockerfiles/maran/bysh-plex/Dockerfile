FROM debian:wheezy
MAINTAINER Tim Haak <tim@haak.co.uk>
#Thanks to https://github.com/bydavy/docker-plex/blob/master/Dockerfile and https://github.com/aostanin/docker-plex/blob/master/Dockerfile

ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8
ENV LC_ALL C.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN apt-get -q update && \
    apt-get install -qy --force-yes curl sudo && \
    echo "deb http://shell.ninthgate.se/packages/debian wheezy main" > /etc/apt/sources.list.d/plexmediaserver.list && \
    curl http://shell.ninthgate.se/packages/shell.ninthgate.se.gpg.key | apt-key add - && \
    apt-get -q update && \
    apt-get -qy --force-yes dist-upgrade && \
    apt-get install -qy --force-yes supervisor ca-certificates procps && \
    apt-get install -qy --force-yes plexmediaserver && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

VOLUME /config
VOLUME /data

ADD ./start.sh /start.sh
RUN chmod u+x  /start.sh

ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 32400

CMD ["/start.sh"]
