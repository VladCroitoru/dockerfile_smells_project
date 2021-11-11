#FROM alpine
FROM martin/openvpn
MAINTAINER LaoGao <noreply@phpgao.com>

ADD sshtl/* /etc/openvpn/
ADD sshtl/ccd /etc/openvpn/ccd
ADD sshtl/pki /etc/openvpn/pki
COPY startopenvpn /usr/local/bin/
RUN chmod +x /usr/local/bin/startopenvpn

ENV SS_VER=3.0.3
ENV SS_URL=https://github.com/shadowsocks/shadowsocks-libev/releases/download/v$SS_VER/shadowsocks-libev-$SS_VER.tar.gz
ENV KCP_VER=20170315
ENV KCP_URL=https://github.com/xtaci/kcptun/releases/download/v$KCP_VER/kcptun-linux-amd64-$KCP_VER.tar.gz

RUN apk --update add --no-cache openssh bash \
  && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
  && echo "root:root" | chpasswd \
  && rm -rf /var/cache/apk/*
RUN sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config
RUN sed -ri 's/#HostKey \/etc\/ssh\/ssh_host_key/HostKey \/etc\/ssh\/ssh_host_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_rsa_key/HostKey \/etc\/ssh\/ssh_host_rsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_dsa_key/HostKey \/etc\/ssh\/ssh_host_dsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ecdsa_key/HostKey \/etc\/ssh\/ssh_host_ecdsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ed25519_key/HostKey \/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config
RUN /usr/bin/ssh-keygen -A
RUN ssh-keygen -t rsa -b 4096 -f  /etc/ssh/ssh_host_key

RUN set -ex && \
    apk add --no-cache --virtual .build-deps \
                                autoconf \
                                build-base \
                                curl \
                                libev-dev \
                                libtool \
                                linux-headers \
                                udns-dev \
                                libsodium-dev \
                                mbedtls-dev \
                                pcre-dev \
                                tar \
                                tzdata \
                                udns-dev && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    cd /tmp && \
    curl -sSL $KCP_URL | tar xz server_linux_amd64 && \
    mv server_linux_amd64 /usr/bin/ && \
    curl -sSL $SS_URL | tar xz --strip 1 && \
    ./configure --prefix=/usr --disable-documentation && \
    make install && \
    cd .. && \
    runDeps="$( \
        scanelf --needed --nobanner /usr/bin/ss-* \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | xargs -r apk info --installed \
            | sort -u \
    )" && \
    apk add --no-cache --virtual .run-deps $runDeps && \
    apk del .build-deps && \
    
    rm -rf /tmp/*

ENV SERVER_ADDR=0.0.0.0 \
SERVER_PORT=3721 \
PASSWORD=laogao \
METHOD=aes-256-cfb \
TIMEOUT=300 \
FASTOPEN=--fast-open \
UDP_RELAY=-u \
USER=nobody \
DNS_ADDR=8.8.8.8 \
DNS_ADDR_2=8.8.4.4


ENV KCP_LISTEN=3824 \
KCP_PASS=phpgao \
KCP_ENCRYPT=aes-192 \
KCP_MODE=fast \
KCP_MUT=1350 \
KCP_NOCOMP=''

EXPOSE $SERVER_PORT/tcp $SERVER_PORT/udp
EXPOSE $KCP_LISTEN/udp 22/tcp 1194/tcp

CMD /usr/sbin/sshd && ss-server -s $SERVER_ADDR \
              -p $SERVER_PORT \
              -k $PASSWORD \
              -m $METHOD \
              -t $TIMEOUT \
              -a $USER \
              $FASTOPEN \
              -d $DNS_ADDR \
              -d $DNS_ADDR_2 \
              $UDP \
              -f /tmp/ss.pid \
              && server_linux_amd64 -t "127.0.0.1:$SERVER_PORT" \
              -l ":$KCP_LISTEN" \
              -key $KCP_PASS \
              --mode $KCP_MODE \
              --crypt $KCP_ENCRYPT \
              --mtu $KCP_MUT \
              $KCP_NOCOMP 
