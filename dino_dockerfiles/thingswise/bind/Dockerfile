FROM ubuntu:14.04
MAINTAINER alexander.s.lukichev@gmail.com

RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y bind9 perl libnet-ssleay-perl openssl \
      libauthen-pam-perl libpam-runtime libio-pty-perl dnsutils \
      apt-show-versions python \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 53/udp 10000/tcp
CMD ["/usr/sbin/named"]
