FROM alpine:3.6

ENV USER=mysql \
    MYSQL_DATA_DIR=/var/lib/mysql \
    MYSQL_SOCKET_DIR=/run/mysqld

RUN set -x \
 && apk add --no-cache \
      mariadb \
      mariadb-client \
      tini \
 && mkdir -p ${MYSQL_SOCKET_DIR}

COPY scripts /usr/local/bin/
COPY mysql   /etc/mysql/

EXPOSE 3306

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["run-root.sh"]

HEALTHCHECK --interval=30s --timeout=1s CMD run-health.sh || exit 1
