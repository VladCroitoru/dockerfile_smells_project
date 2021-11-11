FROM ubuntu:16.04
MAINTAINER Mandus Momberg <mandus@momberg.me>

ENV PDNS_DATABASE="pdns_backend" PDNS_USER="pdns_admin" PDNS_PASSWORD="pdns_admin_password"

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y curl dnsutils

RUN echo "deb http://repo.powerdns.com/ubuntu xenial-auth-master main" >> /etc/apt/sources.list.d/pdns.list && \
echo "Package: pdns-*\nPin: origin repo.powerdns.com\nPin-Priority: 600" > /etc/apt/preferences.d/pdns && \
curl https://repo.powerdns.com/CBC8B383-pub.asc | apt-key add -

RUN cat /etc/apt/preferences.d/pdns

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y pdns-server pdns-backend-mysql
RUN rm /etc/powerdns/pdns.d/*

ADD pdns-init.sql /tmp/
ADD pdns.d/* /etc/powerdns/pdns.d/

ADD pdns-entrypoint.sh /
ENTRYPOINT ["/pdns-entrypoint.sh"]

EXPOSE 53
EXPOSE 53/udp
