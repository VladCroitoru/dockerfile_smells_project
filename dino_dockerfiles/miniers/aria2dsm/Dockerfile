FROM evild/alpine-base:2.0.0
MAINTAINER miniers

ENV RPC_LISTEN_PORT 6800
ENV BT_LISTEN_PORT 51413
ENV DHT_LISTEN_PORT 51415



RUN apk add --no-cache --virtual .build-deps build-base curl \
    && apk add --no-cache --virtual .persistent-deps ca-certificates gnutls-dev expat-dev sqlite-dev c-ares-dev
RUN cd /tmp \
	  && ARIA2_VERSION=`curl "https://github.com/aria2/aria2/releases/latest" | sed -n 's/^.*tag\/release-\(.*\)".*/\1/p'` \
    && curl -fSL https://github.com/aria2/aria2/releases/download/release-${ARIA2_VERSION}/aria2-${ARIA2_VERSION}.tar.xz -o aria2.tar.xz \
    && tar xJf aria2.tar.xz
RUN ARIA2_VERSION=`curl "https://github.com/aria2/aria2/releases/latest" | sed -n 's/^.*tag\/release-\(.*\)".*/\1/p'` \
    && cd /tmp/aria2-${ARIA2_VERSION} \
    && sed -i 's/1, 16/1, -1/g' src/OptionHandlerFactory.cc \
    && ./configure \
    && make -j $(getconf _NPROCESSORS_ONLN) \
    && make install \
    && apk del .build-deps \
    && mkdir -p /etc/aria2 \
	  && mkdir -p /download \
    && rm -rf /tmp

EXPOSE $RPC_LISTEN_PORT $BT_LISTEN_PORT $DHT_LISTEN_PORT

CMD ["/usr/local/bin/aria2c", "--conf-path=/etc/aria2/aria2.conf"]
