FROM verdel/alpine-base:latest
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>

ENV DB_HOST localhost
ENV DB_PORT 3306
ENV DB_USER zabbix
ENV DB_PASS zabbix
ENV DB_NAME zabbix

COPY rootfs /

# Install zabbix
RUN apk --update add \
    bash \
    zabbix-setup@community \
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
