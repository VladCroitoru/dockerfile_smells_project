FROM debian:testing-slim
MAINTAINER Stéphane Alnet <stephane@shimaore.net>

RUN \
  useradd -m opensips && \
  mkdir -p /opt/opensips && \
  chown -R opensips.opensips /opt/opensips

COPY tos.patch /home/opensips/tos.patch

# Install prereqs
ENV MODULES \
  b2b_logic \
  cachedb_redis \
  db_http \
  httpd \
  json \
  rest_client \
  presence \
  presence_mwi \
  presence_dialoginfo \
  proto_tls \
  proto_wss \
  pua \
  pua_dialoginfo \
  tls_mgm

RUN apt-get update && apt-get --no-install-recommends -y install \
  bison \
  build-essential \
  ca-certificates \
  flex \
  git \
  libcurl4-gnutls-dev \
  libjson-c-dev \
  libhiredis-dev \
  libmicrohttpd-dev \
  libncurses5-dev \
  libsctp-dev \
  libssl-dev \
  libxml2-dev \
  m4 \
  netbase \
  patch \
  pkg-config \
  && \
  cd /home/opensips \
  && \
  git clone -b 2.4 https://github.com/OpenSIPS/opensips.git opensips.git && \
  cd opensips.git && \
  git checkout 498aec2a3e7ea7ddeeac95030d7a94b37b2fc47c && \
  cat /home/opensips/tos.patch && \
  patch < /home/opensips/tos.patch && \
  make TLS=1 SCTP=1 prefix=/opt/opensips include_modules="${MODULES}" && \
  make TLS=1 SCTP=1 prefix=/opt/opensips include_modules="${MODULES}" modules && \
  make TLS=1 SCTP=1 prefix=/opt/opensips include_modules="${MODULES}" install && \
  cd .. && \
  rm -rf opensips.git \
  && \
  apt-get purge -y \
  bison \
  build-essential \
  ca-certificates \
  cpp-8 \
  flex \
  gcc-8 \
  git \
  m4 \
  patch \
  pkg-config \
  && apt-get autoremove -y && \
  apt-get install -y \
  libmicrohttpd12 \
  && apt-get clean \
  && rm -rf \
    /opt/opensips/etc/opensips/opensips.cfg \
    /opt/opensips/etc/opensips/tls/ \
  && chown opensips /opt/opensips/etc/opensips/
USER opensips
WORKDIR /home/opensips
