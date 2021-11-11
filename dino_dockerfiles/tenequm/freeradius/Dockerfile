#
# Dockerfile for freeradius
#

FROM alpine:3.4
MAINTAINER tenequm <tenequm@gmail.com>

RUN set -xe \
    && apk add --no-cache freeradius \
                          freeradius-mysql \
                          freeradius-radclient \
                          freeradius-ldap \
                          make \
                          openssl \
    && /etc/raddb/certs/bootstrap \
    && ln -s /etc/raddb/mods-available/sql \
             /etc/raddb/mods-available/sqlcounter /etc/raddb/mods-enabled \
    && sed -i -e 's@driver =.*@driver = "rlm_sql_mysql"@' \
              -e 's@dialect =.*@dialect = "mysql"@' \
              -e '/read_clients = yes/s@^#@@' \
              -e '/Connection info:/,/^$/{s@^#@@;s@localhost@mysql@}' \
              /etc/raddb/mods-available/sql \
    && sed -i -e '/^#\t*eap$/s@^#@@' \
              -e '/^#\teap {$/,/#\t}$/s@^#@@' \
              /etc/raddb/sites-enabled/default \
    && chown -R root:radius /etc/raddb

VOLUME /etc/raddb

EXPOSE 1812/udp 1813/udp

CMD ["radiusd", "-fl", "stdout"]
