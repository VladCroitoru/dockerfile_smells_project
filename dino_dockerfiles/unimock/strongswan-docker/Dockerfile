#
# StrongSwan VPN + Alpine Linux
#

FROM alpine:edge

ARG STRONGSWAN_RELEASE="https://download.strongswan.org/strongswan-5.5.1.tar.bz2"

RUN apk --update add build-base \
            ca-certificates \
            curl \
            bash \
            rsync \
            ip6tables \
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
            --enable-eap-mschapv2 \
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


COPY ./bin/ovw /usr/local/bin/ovw
RUN chmod a+x /usr/local/bin/*

RUN echo ". /etc/profile" > /root/.bashrc
RUN echo "alias ll='ls -alF'"     >> /etc/profile
#RUN echo "export PS1='\H:\w\\$ '" >> /etc/profile
RUN echo 'export TERM="xterm"'    >> /etc/profile


COPY ./entry.sh /entry.sh
RUN chmod a+x   /entry.sh

EXPOSE 500/udp \
       4500/udp

ENTRYPOINT ["/entry.sh"]
CMD ["/usr/sbin/ipsec", "start", "--nofork"]
       
#CMD ["/entry.sh"]
