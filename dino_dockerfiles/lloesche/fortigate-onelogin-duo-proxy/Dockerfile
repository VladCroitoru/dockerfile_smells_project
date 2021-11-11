FROM alpine:edge

WORKDIR /tmp
ADD startup /sbin/startup
ADD https://dl.duosecurity.com/duoauthproxy-latest-src.tgz /tmp/
RUN apk add --no-cache \
    tini python libffi libssl1.0 \
    make gcc bash python-dev libc-dev libffi-dev openssl-dev \
    && tar xzvf duoauthproxy-latest-src.tgz \
    && cd duoauthproxy-*-src \
    && make \
    && cd duoauthproxy-build \
    && ./install --service-user=nobody --install-dir=/duoauthproxy \
    && chmod 755 /sbin/startup \
    && rm -rf /tmp/duoauthproxy-* \
    && apk del --no-cache \
    make gcc bash python-dev libc-dev libffi-dev openssl-dev
ADD authproxy.cfg /duoauthproxy/conf/authproxy.cfg
EXPOSE 1812/udp
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/sbin/startup"]
