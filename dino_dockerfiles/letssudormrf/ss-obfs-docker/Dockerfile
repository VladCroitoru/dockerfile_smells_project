FROM alpine

LABEL maintainer="letssudormrf"

#GIT
ENV SS_GIT_PATH="https://github.com/shadowsocks/shadowsocks-libev" \
    OBFS_GIT_PATH="https://github.com/shadowsocks/simple-obfs" \
    PROXYCHAINS_GIT_PATH="https://github.com/rofl0r/proxychains-ng"

#Download applications
RUN set -ex \
    && apk --update add --no-cache libcrypto1.0 \
                                   libev \
                                   libsodium \
                                   mbedtls \
                                   pcre \
                                   c-ares \
    && apk add --no-cache --virtual TMP git \
                                        autoconf \
                                        automake \
                                        make \
                                        build-base \
                                        zlib-dev \
                                        gettext-dev \
                                        asciidoc \
                                        xmlto \
                                        libpcre32 \
                                        libev-dev \
                                        libsodium-dev \
                                        libtool \
                                        linux-headers \
                                        mbedtls-dev \
                                        openssl-dev \
                                        pcre-dev \
                                        c-ares-dev \
                                        g++ \
                                        gcc \

#Compile Shadowsocks + simple-obfs + proxychains
   && cd /tmp \
   && git clone ${SS_GIT_PATH} \
   && cd ${SS_GIT_PATH##*/} \
   && git submodule update --init --recursive \
   && ./autogen.sh \
   && ./configure --prefix=/usr && make \
   && make install \
   && cd /tmp \
   && git clone ${OBFS_GIT_PATH} \
   && cd ${OBFS_GIT_PATH##*/} \
   && git submodule update --init --recursive \
   && ./autogen.sh \
   && ./configure --prefix=/usr && make \
   && make install \
   && cd /tmp \
   && git clone ${PROXYCHAINS_GIT_PATH} \
   && cd ${PROXYCHAINS_GIT_PATH##*/} \
   && ./configure --prefix=/usr --sysconfdir=/etc && make \
   && make install && make install-config \
   && cd \
   && apk del TMP \
   && rm -rf /tmp/* \
   && rm -rf /var/cache/apk/*

COPY entrypoint.sh /usr/local/bin/
RUN chmod a+rwx /usr/local/bin/entrypoint.sh

EXPOSE 8443/tcp 8443/udp

CMD ["entrypoint.sh"]
