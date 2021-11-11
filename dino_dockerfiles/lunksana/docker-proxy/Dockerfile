FROM alpine:latest
LABEL maintainer="lunksana <zoufeng4@gmail.com>"

#ENV BUILDPATH="git make linux-headers autoconf automake libtool gcc libc-dev"
#ENV METHODPATH="pcre-dev libev-dev libsodium-dev c-ares-dev mbedtls-dev rng-tools"
ENV SERVER_HOST=0.0.0.0
ENV SERVER_PORT=10000
ENV PASSWORD="password"
ENV METHOD="chacha20-ietf-poly1305"
ENV PLUGIN="obfs-server"
ENV PLUGIN_OPTS=
ENV PLUGIN_OPTS_LOCAL=
ENV SS_MOD="ss-server"
ENV ENABLE_OBFS="false"

RUN apk update \
    && apk upgrade

#RUN apk add ${BUILDPATH} \
#    && apk add ${METHODPATH} \
RUN apk add --no-cache rng-tools
RUN apk add --no-cache --virtual .build-deps \
    autoconf \
    automake \
    build-base \
    c-ares-dev \
    libev-dev \
    libtool \
    libsodium-dev \
    linux-headers \
    mbedtls-dev \
    pcre-dev \
    git \
    && mkdir /ss \
    && (cd /ss \
    && git clone https://github.com/shadowsocks/shadowsocks-libev \
    && git clone https://github.com/shadowsocks/simple-obfs \
    && (cd shadowsocks-libev \
    && git submodule update --init --recursive \
    && ./autogen.sh \
    && ./configure --prefix=/usr --disable-documentation \
    && make && make install) \
    && (cd /ss/simple-obfs \
    && git submodule update --init --recursive \
    && ./autogen.sh \
    && ./configure --disable-documentation  \
    && make && make install)) \
    && rm -rf /ss \
    && rm -rf /usr/local/bin/ss-redir \
    && rm -rf /usr/local/bin/ss-manager \
    && rm -rf /usr/local/bin/ss-nat \
    && rm -rf /usr/local/bin/ss-tunnel \
#    && apk del ${BUILDPATH} \
#    && rm -rf /var/cache/apk/*
    && apk add --no-cache \
        $(scanelf --needed --nobanner /usr/bin/ss-* /usr/local/bin/obfs-* \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | xargs -r apk info --installed \
        | sort -u) \
    && apk del .build-deps

ADD start.sh /
RUN chmod +x /start.sh
EXPOSE 10000
EXPOSE 10000/udp
ENTRYPOINT [ "/start.sh" ]