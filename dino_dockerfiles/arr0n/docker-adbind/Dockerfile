FROM phusion/baseimage
MAINTAINER arr0n

# this is completely ripped off from Sameersbn bind image -->> https://github.com/sameersbn/docker-bind

ENV DATA_DIR=/data \
    BIND_USER=bind \
    WEBMIN_VERSION=1.760

RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \
 && apt-get update && apt-get upgrade -y \
 && apt-get install -y wget bind9 perl libnet-ssleay-perl openssl \
      libauthen-pam-perl libpam-runtime libio-pty-perl \
      apt-show-versions python \
 && wget "http://prdownloads.sourceforge.net/webadmin/webmin_${WEBMIN_VERSION}_all.deb" -P /tmp/ \
 && dpkg -i /tmp/webmin_${WEBMIN_VERSION}_all.deb \
 && rm -rf /tmp/webmin_${WEBMIN_VERSION}_all.deb \
 && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

# Ad-blocking stuff 
ADD dc-bind-ad-block.sh /etc/bind/dc-bind-ad-block.sh
ADD dummy.null.zone.file /etc/bind/null.zone.file
RUN echo 'include "/etc/bind/blacklist";' >> /etc/bind/named.conf && \
	touch /etc/bind/blacklist

EXPOSE 53/udp 10000/tcp
VOLUME ["${DATA_DIR}"]
ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["/usr/sbin/named"]
