FROM busybox:latest

ADD https://busybox.net/downloads/binaries/ssl_helper-x86_64 /bin/ssl_helper

RUN chmod 755 /bin/ssl_helper

ENV SHADOWSOCKS_SERVER_VERSION=1.2.1
ENV SHADOWSOCKS_CLIENT_VERSION=1.1.5

RUN wget -O /tmp/ss.tar.gz https://github.com/shadowsocks/shadowsocks-go/releases/download/${SHADOWSOCKS_SERVER_VERSION}/shadowsocks-server.tar.gz \
    && wget -O /tmp/sl.gz https://github.com/shadowsocks/shadowsocks-go/releases/download/${SHADOWSOCKS_CLIENT_VERSION}/shadowsocks-local-linux64-${SHADOWSOCKS_CLIENT_VERSION}.gz \
    && tar xzvf /tmp/ss.tar.gz -C /tmp && mv /tmp/shadowsocks-server /bin/ssserver \
    && gunzip -c /tmp/sl.gz > /bin/sslocal \
    && rm -rf /tmp/*.gz \
    && chmod +x /bin/ss*

COPY entrypoint.sh .

COPY config.json .

EXPOSE 443

ENTRYPOINT ["sh", "entrypoint.sh"]
