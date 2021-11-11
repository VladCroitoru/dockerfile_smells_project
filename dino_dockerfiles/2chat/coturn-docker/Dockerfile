FROM alpine:latest
MAINTAINER Roman Gordeev <roma.gordeev@gmail.com>

ENV COTURN_VERSION 4.5.0.6


RUN mkdir /src

RUN set -x && \
 apk add --no-cache --update bash curl wget make \
 build-base automake autoconf readline readline-dev \
 gettext libcrypto1.0 libressl libressl-dev libevent \
 libevent-dev linux-headers jq

WORKDIR /src

RUN set -x && \
  wget --no-check-certificate https://github.com/coturn/coturn/archive/${COTURN_VERSION}.tar.gz && \
  tar zxf ${COTURN_VERSION}.tar.gz && \
  rm ${COTURN_VERSION}.tar.gz

WORKDIR /src/coturn-${COTURN_VERSION}
RUN set -x && \
    ./configure && \
    make install && \
    rm -rf /src && \
    rm -rf /var/cache/apk/*

# STUN/TURN UDP
EXPOSE 3478/udp
# STUN/TURN TCP
EXPOSE 3478/tcp
# STUN/TURN UDP Alt port (RFC5780 support)
EXPOSE 3479/udp
# STUN/TURN TCP Alt port (RFC5780 support)
EXPOSE 3479/tcp
# STUN/TURN DTLS
EXPOSE 5349/udp
# STUN/TURN TLS
EXPOSE 5349/tcp
# STUN/TURN DTLS Alt port (RFC5780 support)
EXPOSE 5350/udp
# STUN/TURN TLS Alt port (RFC5780 support)
EXPOSE 5350/tcp
# UDP media ports for TURN relay
EXPOSE 20000-65535/udp

ADD coturn.sh /coturn.sh
RUN chmod u+rx /coturn.sh

CMD /coturn.sh
