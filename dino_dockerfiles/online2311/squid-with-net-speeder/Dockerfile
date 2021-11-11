FROM ubuntu:14.04.3
MAINTAINER zhangjing@189csp.com

ENV SQUID_VERSION=3.3.8 \
    SQUID_CACHE_DIR=/var/spool/squid3 \
    SQUID_LOG_DIR=/var/log/squid3 \
    SQUID_USER=proxy

RUN apt-get update \
	&&  apt-get install libnet1 libpcap0.8 \
	&&  apt-get install -y libnet1-dev libpcap0.8-dev git apache2-utils \
	&&  apt-get clean

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 80F70E11F0F0D5F10CB20E62F5DA5F09C3173AA6 \
 && echo "deb http://ppa.launchpad.net/brightbox/squid-ssl/ubuntu trusty main" >> /etc/apt/sources.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y squid3-ssl=${SQUID_VERSION}* \
 && mv /etc/squid3/squid.conf /etc/squid3/squid.conf.dist \
 && rm -rf /var/lib/apt/lists/*

COPY squid.conf /etc/squid3/squid.conf
COPY radius_config /etc/radius_config
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh
RUN mkdir /usr/etc/
RUN htpasswd -c -b /usr/etc/passwd 189csp Hello189
RUN git clone https://github.com/snooda/net-speeder.git net-speeder
WORKDIR net-speeder
RUN sh build.sh

RUN mv net_speeder /usr/local/bin/
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/net_speeder

EXPOSE 1080/tcp
VOLUME ["${SQUID_CACHE_DIR}","/usr/etc"]
ENTRYPOINT ["/sbin/entrypoint.sh"]
