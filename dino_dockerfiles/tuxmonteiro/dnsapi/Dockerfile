FROM ubuntu:xenial

MAINTAINER tuxmonteiro

ENV DEBIAN_FRONTEND="noninteractive"

EXPOSE 8000 53/udp 5353/udp

RUN echo "pdns-backend-sqlite3 pdns-backend-sqlite3/dbconfig-install boolean true" | /usr/bin/debconf-set-selections; \
    apt-get update -y ; \
    apt install -y pdns-backend-sqlite3 bind9 dnsutils curl

ADD pdns2bind.sh /tmp/
ADD start.sh /tmp/
ADD named.conf.options /etc/bind/
ADD pdns.conf /etc/powerdns/

CMD ["/tmp/start.sh"]
