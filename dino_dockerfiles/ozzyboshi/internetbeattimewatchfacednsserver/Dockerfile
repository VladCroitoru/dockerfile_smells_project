FROM debian:jessie
MAINTAINER gun101@email.it

ENV BIND_USER=bind \
    BIND_VERSION=1:9.9.5 \
    WEBMIN_VERSION=1.8 \
    DATA_DIR=/data \
    VERSION_DATE=20170117

RUN apt-get update && apt-get install -y wget curl

RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \
 && wget http://www.webmin.com/jcameron-key.asc -qO - | apt-key add - \
 && echo "deb http://download.webmin.com/download/repository sarge contrib" >> /etc/apt/sources.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y bind9=${BIND_VERSION}* bind9-host=${BIND_VERSION}* webmin=${WEBMIN_VERSION}* \
 && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

ADD named.conf.local /data/bind/etc/named.conf.local
ADD internetbeattimewatchface.ozzy-boshi.com.hosts /data/bind/lib/internetbeattimewatchface.ozzy-boshi.com.hosts
ADD internetbeattimewatchface.ozzy-boshi.info.hosts /data/bind/lib/internetbeattimewatchface.ozzy-boshi.info.hosts
ADD internetwatchfacelist.txt /root/internetwatchfacelist.txt
ADD https://gist.githubusercontent.com/Ozzyboshi/4c2c0817764c88459337d94e2e907e04/raw/d693c97cbea9132b30a74d33aef17eb82783c6a1/dnsupdater.sh /root/dnsupdater.sh
RUN chmod 755 /root/dnsupdater.sh

EXPOSE 53/udp 53/tcp 10000/tcp

ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["/usr/sbin/named"]

