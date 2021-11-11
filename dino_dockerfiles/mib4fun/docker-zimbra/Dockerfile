#################################################################
# Dockerfile to build Zimbra Collaboration 8.6 container images
# Based on Ubuntu 14.04
# Created by Jorge de la Cruz
#################################################################
FROM ubuntu:14.04
MAINTAINER Jorge de la Cruz <jorgedlcruz@gmail.com>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \
  wget \
  bind9 \
  bind9utils \
  bind9-doc \
  dnsutils \
  libidn11 \
  libpcre3 \
  libgmp10 \
  libexpat1 \
  libstdc++6 \
  libperl5.18 \
  libaio1 \
  netcat-openbsd \
  pax \
  resolvconf \
  sqlite3 \
  sudo \
  sysstat \
  unzip

VOLUME ["/opt/zimbra"]

EXPOSE 22 25 456 587 110 143 993 995 80 443 8080 8443 7071

COPY opt /opt/

COPY etc /etc/

CMD ["/bin/bash", "/opt/start.sh"]
