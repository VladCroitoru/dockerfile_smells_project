FROM alpine:latest

ENV TERM=xterm-color

ENV STRONGSWAN_RELEASE https://download.strongswan.org/strongswan.tar.bz2

RUN apk --update add build-base \
            ca-certificates \
            curl \
            mc \
            nano \
            supervisor \
            bash \
            iproute2 \
            iptables-dev \
            openssl \
            openssl-dev && \
    mkdir -p /tmp/strongswan && \
    curl -Lo /tmp/strongswan.tar.bz2 $STRONGSWAN_RELEASE && \
    tar --strip-components=1 -C /tmp/strongswan -xjf /tmp/strongswan.tar.bz2 && \
    cd /tmp/strongswan && \
    ./configure --prefix=/usr \
            --sysconfdir=/etc \
            --libexecdir=/usr/lib \
            --with-ipsecdir=/usr/lib/strongswan \
            --enable-aesni \
            --enable-chapoly \
            --enable-cmd \
            --enable-dhcp \
            --enable-eap-dynamic \
            --enable-eap-identity \
            --enable-eap-md5 \
            --enable-eap-radius \
            --enable-eap-tls \
            --enable-farp \
            --enable-files \
            --enable-gcm \
            --enable-md4 \
            --enable-newhope \
            --enable-ntru \
            --enable-openssl \
            --enable-sha3 \
            --enable-shared \
            --disable-aes \
            --disable-des \
            --disable-gmp \
            --disable-hmac \
            --disable-ikev1 \
            --disable-md5 \
            --disable-rc2 \
            --disable-sha1 \
            --disable-sha2 \
            --disable-static && \
    make && \
    make install && \
    rm -rf /tmp/* && \
    apk del build-base curl openssl-dev && \
    rm -rf /var/cache/apk/*

    RUN mkdir -p /data/configs

    COPY ./conf/ipsec.conf /data/configs/ipsec.conf
    COPY ./conf/firewall.updown /data/configs/firewall.updown

    COPY ./conf/strongswan.conf /etc/strongswan.conf
    COPY ./conf/ipsec.secrets /etc/ipsec.secrets
    COPY ./conf/supervisord.conf /etc/supervisord.conf

    COPY ./scripts /data/bin

    EXPOSE 8080
    EXPOSE 500:500/udp
    EXPOSE 4500:4500/udp

    ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
