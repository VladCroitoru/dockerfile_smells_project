FROM alpine:latest

ARG DDCLIENT_VERSION=3.8.3

RUN apk add --no-cache --virtual build-dependencies \
    bzip2 \
    curl \
    gcc \
    make \
    tar \
    wget \
  && apk add --no-cache \
    net-tools \
    bash \
    perl \
    perl-digest-sha1 \
    perl-io-socket-ssl \
    perl-json \
  && curl -L http://cpanmin.us | perl - App::cpanminus \
  && cpanm --notest JSON::Any \
  && curl -L -o /tmp/ddclient-${DDCLIENT_VERSION}.tar.bz2 http://downloads.sourceforge.net/project/ddclient/ddclient/ddclient-${DDCLIENT_VERSION}.tar.bz2 \
  && mkdir /tmp/ddclient \
  && tar xf /tmp/ddclient-${DDCLIENT_VERSION}.tar.bz2 -C /tmp/ddclient --strip-components=1 \
  && install -Dm755 /tmp/ddclient/ddclient /usr/bin/ \
  && mkdir /var/cache/ddclient /etc/ddclient \
  && apk del --purge build-dependencies \
  && rm -rf /config/.cpanm /root/.cpanm /tmp/*

COPY entrypoint.sh .

ENTRYPOINT ["sh", "/entrypoint.sh", "start-service"]
