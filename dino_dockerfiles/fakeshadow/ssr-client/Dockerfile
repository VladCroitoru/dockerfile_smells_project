FROM alpine:3.5

MAINTAINER shadou <shadou@erhuo.two>

WORKDIR /root

ENV SSR_VERSION 3.0.1

RUN apk upgrade --no-cache \
    && apk add --no-cache bash tzdata python py-setuptools wget libsodium \
    && wget --no-check-certificate https://github.com/shadowsocksr/shadowsocksr/archive/$SSR_VERSION.tar.gz \
    && tar -zxvf $SSR_VERSION.tar.gz \
    && (cd /root/shadowsocksr-$SSR_VERSION && python setup.py install)  \
    && apk del wget \
    && rm -f $SSR_VERSION.tar.gz \
    && rm -rf shadowsocksr-$SSR_VERSION \
    rm -rf /var/cache/apk/*

CMD sslocal -s ${SERVER_ADDR:-0.0.0.0} \
            -p ${SERVER_PORT:-80} \
            -k ${PASSWORD:-$(hostname)} \
            -b ${LOCAL_ADDR:-127.0.0.1} \
            -l ${LOCAL_PORT:-1081} \
            -m ${METHOD:-chacha20-ietf} \
	        -O ${PROTOCOL:-auth_aes128_sha1} \
            -G ${PROTOCOL_PARAM:-} \
            -o ${OBFS:-tls1.2_ticket_auth} \
            -g ${OBFS_PARAM:-www.189.cn} \
            -t ${TIMEOUT:-120} \
            --fast-open
