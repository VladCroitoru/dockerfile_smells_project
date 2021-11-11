FROM ubuntu:14.04.2

ENV SQUID_VERSION=3.3.8 \
    SQUID_CACHE_DIR=/var/spool/squid3 \
    SQUID_LOG_DIR=/var/log/squid3 \
    SQUID_USER=proxy

RUN apt-get update
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 80F70E11F0F0D5F10CB20E62F5DA5F09C3173AA6 \
 && echo "deb http://ppa.launchpad.net/brightbox/squid-ssl/ubuntu trusty main" >> /etc/apt/sources.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y squid3-ssl=${SQUID_VERSION}* \
 && mv /etc/squid3/squid.conf /etc/squid3/squid.conf.dist \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y apt-cacher-ng supervisor
RUN apt-get install -y python python-pip
RUN pip install -q -U devpi-server

COPY squid.conf /etc/squid3/squid.conf
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir /scripts
COPY *.sh /scripts/
RUN chmod 755 /scripts/*.sh

VOLUME ["${SQUID_CACHE_DIR}"]
VOLUME ["/var/cache/apt-cacher-ng"]
VOLUME ["/var/.devpi/server"]

EXPOSE 3128
EXPOSE 3141
EXPOSE 3142

CMD /usr/bin/supervisord -n
