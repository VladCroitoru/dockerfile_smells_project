FROM anapsix/alpine-java:7_jdk

ADD finalspeed_server.zip /finalspeed_server.zip
RUN apk update \
    && apk add python libsodium unzip wget iptables libcap  libcap-dev \
    && rm -rf /var/cache/apk/* \
    && mkdir /ssr \
    && cd /ssr \
    && wget --no-check-certificate https://github.com/breakwa11/shadowsocks/archive/manyuser.zip -O /tmp/manyuser.zip \
    && unzip -d /tmp /tmp/manyuser.zip \
    && mv /tmp/shadowsocksr-manyuser/shadowsocks /ssr/shadowsocks \
    && rm -rf /tmp/* \
    && cd / \
    && unzip -o finalspeed_server.zip -d /fs \ 
    && apk del  wget  unzip

COPY config.json /config.json
COPY dns.conf /ssr/shadowsocks/dns.conf

EXPOSE 150/udp 150/tcp
EXPOSE 8765
EXPOSE 8766

ADD start.sh /start.sh
RUN chmod 755 /start.sh

CMD ["sh", "-c", "/start.sh"]
