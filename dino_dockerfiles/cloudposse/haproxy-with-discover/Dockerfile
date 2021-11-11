FROM cloudposse/haproxy

ENV ETCD_HOST 172.17.42.1
ENV ETCD_PORT 4001
ENV CONFD_VERSION 0.9.0
ENV CONFD_INTERVAL 60
ENV CONFD_PREFIX /haproxy
ENV HAPROXY_MODE http

# To work around a bug in systemd not handling escaping in CoreOS 717.1.0
#ENV HAPROXY_CHECK "HEAD / HTTP/1.1\r\nHost:localhost"
ENV HAPROXY_CHECK_METHOD HEAD
ENV HAPROXY_CHECK_PATH /
ENV HAPROXY_CHECK_VERSION HTTP/1.1
ENV HAPROXY_CHECK_HOST localhost
ENV HAPROXY_BIND_OPTIONS=
ENV HAPROXY_NAMESERVER=

ADD https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-linux-amd64 /usr/bin/confd

RUN chmod 755 /usr/bin/confd && \
    sed -i s/ENABLED=0/ENABLED=1/g /etc/default/haproxy 
ADD start /start
ADD reload /reload
ADD confd/ /etc/confd

ENTRYPOINT ["/start"]

