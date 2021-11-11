# Multistage docker build, requires docker 17.05

# builder stage
FROM alpine:edge as builder

ARG TRANSMISSION_VER=3.00-seq1
ARG BUILD_CORES

RUN NB_CORES=${BUILD_CORES-`getconf _NPROCESSORS_CONF`} \
 && BUILD_DEPS=" \
    build-base \
    patch \
    libtool \
    libevent-dev \
    automake \
    autoconf \
    cmake \
    wget \
    tar \
    xz \
    zlib-dev \
    cppunit-dev \
    libressl-dev \
    ncurses-dev \
    curl-dev \
    binutils \
    git" \
 && apk -U upgrade && apk add \
    ${BUILD_DEPS} \
    ca-certificates \
    curl \
    libressl \
    gzip \
    zip \
    zlib \
    unrar \
    s6 \
    su-exec \
    libevent \
    jq \
 && rm -rf /var/cache/apk/* /tmp/*

RUN cd /tmp \
 && git clone --depth 1 --branch ${TRANSMISSION_VER} https://github.com/Mikayex/transmission.git Transmission \
 && cd Transmission \
 && git submodule update --init \
 && mkdir build && cd build && cmake .. && make -j ${NB_CORES} && make install \
 && strip -s /usr/local/bin/transmission-daemon

# runtime stage
FROM alpine:edge

ENV UID=991 GID=991 \
    FLOOD_SECRET=supersecret

COPY --from=builder /usr/local/share/transmission/web /usr/local/share/transmission/web
COPY --from=builder /usr/local/share/doc/transmission /usr/local/share/doc/transmission
COPY --from=builder /usr/local/bin/transmission-* /usr/local/bin/
COPY --from=builder /usr/local/share/man/man1/transmission-* /usr/local/share/man/man1/

RUN apk -U upgrade && apk add \
     ca-certificates \
     curl \
     libressl \
     gzip \
     zip \
     zlib \
     unrar \
     s6 \
     su-exec \
     libevent \
     jq \
 && rm -rf /var/cache/apk/* /tmp/*

COPY s6.d /etc/s6.d
COPY run.sh /usr/bin/
COPY default-settings.json /default-settings.json

RUN chmod +x /usr/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*

VOLUME /home/transmission/.config/transmission-daemon /home/transmission/Downloads

EXPOSE 9091

LABEL description="BitTorrent client with WebUI front-end" \
      transmission="Transmission BiTorrent client v$TRANSMISSION_VER" \
      maintainer="lndvll <lndvll@targaryen.house>"

CMD ["run.sh"]
