FROM verdel/alpine-base:latest
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>

ENV DB_HOST db
ENV DB_PORT 3306
ENV DB_NAME cattle
ENV DB_USER cattle
ENV DB_PASS cattle

COPY rootfs /

# Install zabbix
RUN apk --update add \
    bash \
    mysql-client \
    # Clean up
    && rm -rf \
    /usr/share/man \
    /tmp/* \
    /var/cache/apk/*

# Copy scripts
RUN chmod 755 /sbin/*.sh

# Export volumes directory
VOLUME ["/backup"]

ENTRYPOINT ["/sbin/entrypoint.sh"]