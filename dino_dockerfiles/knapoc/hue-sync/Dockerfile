FROM alpine

ARG SHAIRPORT_VERSION=master

RUN apk add --update \
        git \
        build-base \
        autoconf \
        automake \
        libtool \
        libstdc++ \
        curl curl-dev \
        fftw fftw-dev \
        libdaemon libdaemon-dev \
        popt popt-dev \
        libconfig libconfig-dev \
        alsa-lib alsa-lib-dev \
        avahi-libs avahi-dev \
        openssl openssl-dev \
        soxr soxr-dev \
    && ldconfig / \
    && cd /tmp \
    && git clone -b $SHAIRPORT_VERSION --depth=1 --single-branch https://github.com/kwasmich/shairport-sync.git \
      && cd shairport-sync \
    && autoreconf -i -f  \
    && ./configure \
                   CFLAGS='-I/opt/vc/include -I/opt/vc/include/interface/vcos/pthreads -I/opt/vc/include/interface/vmcs_host/linux' \
                   LDFLAGS='-L/opt/vc/lib' \
                   --with-hue \
                   --with-alsa \
  		             --with-avahi \
  		             --with-ssl=openssl \
  		             --with-soxr \
  		             --with-metadata \
    && make \
    && make install \
    && cd \
    && apk del \
        git \
        build-base \
        autoconf \
        automake \
        libdaemon-dev \
        popt-dev \
        libconfig-dev \
        alsa-lib-dev \
        avahi-dev \
        openssl-dev \
        soxr-dev \
        curl \
        curl-dev \
        fftw-dev \
    && apk add --update \
        curl \
        dbus \
        alsa-lib \
        fftw \
        libdaemon \
        popt \
        openssl \
        soxr \
        avahi \
        libconfig \
    && rm -rf \
        /tmp/shairport-sync \
        /lib/apk/db/* \
        /etc/ssl \
        /usr/local/etc/shairport-sync* \
        /var/cache/apk/*

COPY start.sh /start.sh

RUN chmod a+x /start.sh

ENV HUE_BRIDGE_IP 0.0.0.0
ENV BRIDGE_ACCESS_IDENTIFIER randomidentifier
ENV HUE_LAMP_COUNT 1,2,3
ENV AIRPLAY_NAME hue-sync-docker
ENV HUE_SYNC_PORT 5001

ENTRYPOINT [ "/start.sh" ]
